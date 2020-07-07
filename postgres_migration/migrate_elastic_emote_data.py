import yaml
import asyncio
from postgres_migration.elastic import ElasticSearchClient
from aiopg import connect


async def main(config):
    client = ElasticSearchClient(hosts=config["elastic_uri"])
    async with client as db:
        async with connect(config["postgres_uri"]) as conn:
            async with conn.cursor() as cur:
                i = 0

                async for model in db._scroll(index="extra_emote", body={}):
                    i += 1
                    if i % 10000 == 0:
                        print(f"Loading emote {i}")

                    emote_id = model["_id"]
                    src = model["_source"]
                    is_animated = src["is_animated"]
                    shas = src["shas"]
                    ids = src["ids"]
                    names = src["names"]

                    is_nsfw = src.get("filtered", False)
                    always_filter = False
                    times_used = src.get("times_used", 0)

                    external_id = src["external_id"]
                    external_service = src["external_service"]
                    external_url = src["external_url"]

                    if not ids:
                        continue

                    await cur.execute(
                        "INSERT INTO emote_ids (emote_hash, emote_id, usable, animated) (SELECT %(emote_hash)s, *, true, %(animated)s FROM UNNEST(%(emote_ids)s)) ON CONFLICT DO NOTHING",
                        parameters={
                            "emote_hash": emote_id,
                            "emote_ids": [int(i) for i in ids],
                            "animated": is_animated
                        }
                    )


if __name__ == "__main__":
    with open("../config.yaml") as conf_file:
        config = yaml.load(conf_file, Loader=yaml.SafeLoader)

    asyncio.run(main(config))
