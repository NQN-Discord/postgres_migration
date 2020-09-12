def up(cursor):
    cursor.execute("alter table user_packs add constraint user_packs_packs_guild_id_fk foreign key (guild_id) references packs on delete cascade;")


def down(cursor):
    cursor.execute("alter table user_packs drop constraint user_packs_packs_guild_id_fk;")
