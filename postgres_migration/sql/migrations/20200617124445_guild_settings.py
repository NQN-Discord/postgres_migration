

def up(cursor):
    cursor.execute(
        """
        create table guild_settings (
            guild_id             bigint                                 not null
                constraint guild_settings_pk
                    primary key,
            prefix               varchar default '!'::character varying not null,
            announcement_channel bigint,
            boost_channel        bigint,
            boost_role           bigint,
            audit_channel        bigint,
            enable_stickers      boolean default true,
            enable_nitro         boolean default true,
            enable_replies       boolean default true,
            enable_masked_links  boolean default true,
            is_alias_server      boolean default false
        );
        """
    )

    cursor.execute("create index guild_settings_alias_servers on guild_settings (is_alias_server);")


def down(cursor):
    cursor.execute("drop table guild_settings")
