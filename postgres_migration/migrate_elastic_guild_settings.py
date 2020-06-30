import yaml
import asyncio
from postgres_migration.elastic import ElasticSearchClient
from aiopg import connect


async def main(config):
    client = ElasticSearchClient(hosts=config["elastic_uri"])
    async with client as db:
        async with connect(config["postgres_uri"]) as conn:
            async with conn.cursor() as cur:
                async for model in db._scroll(index="guild_settings", body={}):
                    await cur.execute(
                        "INSERT INTO guild_settings VALUES (%(guild_id)s, %(prefix)s, %(announcement_channel)s, %(boost_channel)s, %(boost_role)s, %(audit_channel)s, %(enable_stickers)s, %(enable_nitro)s, %(enable_replies)s, %(enable_masked_links)s, %(is_alias_server)s) ON CONFLICT DO NOTHING",
                        parameters={
                            "guild_id": model["_id"],
                            "prefix": model.get("prefix", "!"),
                            "announcement_channel": model.get("announcement_channel", None),
                            "boost_channel": model.get("boost_channel", None),
                            "boost_role": model.get("boost_role", None),
                            "audit_channel": model.get("audit_channel", None),
                            "enable_stickers": model.get("enable_stickers", True),
                            "enable_nitro": model.get("enable_nitro", True),
                            "enable_replies": model.get("enable_replies", True),
                            "enable_masked_links": model.get("enable_masked_links", True),
                            "is_alias_server": model.get("is_alias_server", False)
                        }
                    )


if __name__ == "__main__":
    with open("../config.yaml") as conf_file:
        config = yaml.load(conf_file, Loader=yaml.SafeLoader)

    asyncio.run(main(config))
