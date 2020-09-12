def up(cursor):
    cursor.execute("""
    create table packs
    (
        guild_id bigint not null,
        pack_name varchar not null,
        is_public boolean not null
    );
    """)
    cursor.execute("create index packs_pack_name_index on packs (pack_name);")
    cursor.execute("create unique index packs_guild_id_uindex on packs (guild_id);")
    cursor.execute("alter table packs add constraint packs_pk primary key (guild_id);")


def down(cursor):
    cursor.execute("drop table packs")
