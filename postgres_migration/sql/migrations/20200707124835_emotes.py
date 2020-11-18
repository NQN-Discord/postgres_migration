def up(cursor):
    cursor.execute("""
    create table emote_ids
    (
        emote_id bigint,
        emote_hash char(64),
        usable bool default true,
        animated bool
    );
    
    create index emote_ids_emote_hash_uindex
        on emote_ids (emote_hash);
    
    alter table emote_ids
        add constraint emote_ids_pk
            primary key (emote_id);
    """)


def down(cursor):
    cursor.execute("drop table emote_ids")
