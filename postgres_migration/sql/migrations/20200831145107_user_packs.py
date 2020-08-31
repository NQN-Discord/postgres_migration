def up(cursor):
    cursor.execute("create table user_packs (user_id bigint not null, guild_id bigint not null);")
    cursor.execute("create index ix_user_packs_guild_id_user_id on user_packs (guild_id, user_id);")
    cursor.execute("create index ix_user_packs_user_id on user_packs (user_id);")


def down(cursor):
    cursor.execute("drop table user_packs")
