# -*- coding: utf-8 -*-


def up(cursor):
    cursor.execute("""
        create table stickers
        (
            prefix varchar not null,
            suffix varchar not null,
            owner_id bigint not null,
            constraint stickers_pk
                primary key (suffix, prefix)
        );
    """)
    cursor.execute("create index stickers_prefix_suffix_index on stickers (prefix, suffix);")
    cursor.execute("create index stickers_suffix_index on stickers (suffix);")


def down(cursor):
    cursor.execute("DROP TABLE stickers;")
