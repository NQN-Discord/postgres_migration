import yaml
import asyncio
from elastic import ElasticSearchClient
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
                            **model["_source"]
                        }
                    )


if __name__ == "__main__":
    with open("config.yaml") as conf_file:
        config = yaml.load(conf_file, Loader=yaml.SafeLoader)

    asyncio.run(main(config))
