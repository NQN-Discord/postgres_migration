def up(cursor):
    cursor.execute("alter table user_packs add constraint user_packs_packs_guild_id_fk foreign key (guild_id) references packs on delete cascade;")
    cursor.execute("create unique index packs_pack_name_uindex on packs (pack_name);")


def down(cursor):
    cursor.execute("alter table user_packs drop constraint user_packs_packs_guild_id_fk;")
    cursor.execute("drop index packs_pack_name_uindex;")
