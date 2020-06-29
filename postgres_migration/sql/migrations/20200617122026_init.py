
def up(cursor):
    cursor.execute("create table members (user_id  bigint, guild_id bigint)")
    cursor.execute("create index ix_members_guild_id_user_id on members (guild_id, user_id);")
    cursor.execute("create index ix_members_user_id on members (user_id);")


def down(cursor):
    cursor.execute("drop table members")
