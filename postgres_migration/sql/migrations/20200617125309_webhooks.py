def up(cursor):
    cursor.execute(
        """
        create table webhooks
        (
            webhook_id bigint not null
                constraint webhooks_pk
                    primary key,
            guild_id   bigint not null,
            channel_id bigint not null,
            token      text   not null,
            name       text   not null
        );
        """
    )
    cursor.execute("create index webhooks__index_guild_channel on webhooks (guild_id, channel_id);")
    cursor.execute("create index webhooks_channel_id_index on webhooks (channel_id);")


def down(cursor):
    cursor.execute("drop table webhooks")
