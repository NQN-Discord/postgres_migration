import yaml
import asyncio
from elastic import ElasticSearchClient
from aiopg import connect


async def main(config):
    client = ElasticSearchClient(hosts=config["elastic_uri"])
    async with client as db:
        async with connect(config["postgres_uri"]) as conn:
            async with conn.cursor() as cur:
                async for model in db._scroll(index="webhook", body={}):
                    await cur.execute(
                        "INSERT INTO webhooks VALUES (%(webhook_id)s, %(guild_id)s, %(channel_id)s, %(token)s, %(name)s) ON CONFLICT DO NOTHING",
                        parameters={
                            "webhook_id": model["_id"],
                            **model["_source"]
                        }
                    )


if __name__ == "__main__":
    with open("config.yaml") as conf_file:
        config = yaml.load(conf_file, Loader=yaml.SafeLoader)

    asyncio.run(main(config))
