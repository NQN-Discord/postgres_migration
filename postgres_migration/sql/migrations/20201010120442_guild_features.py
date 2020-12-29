def up(cursor):
    cursor.execute("CREATE TYPE guild_features_enum AS ENUM ('emote_roles')")
    cursor.execute("""
        create table guild_features
        (
            guild_id bigint not null,
            feature guild_features_enum not null,
            unique (guild_id, feature)
        );
    """)
    cursor.execute("create index guild_features_feature_index on guild_features (feature)")
    cursor.execute("create index guild_features_guild_id_index on guild_features (guild_id)")
    cursor.execute("alter table guild_settings rename column announcement_channel to nitro_role")
    cursor.execute("alter table guild_settings add enable_pings boolean default true")
    cursor.execute("alter table guild_settings add max_guildwide_emotes int default 10")

    cursor.execute("CREATE TYPE premium_last_charge_status_enum AS ENUM ('Paid', 'Declined', 'Deleted', 'Pending', 'Refunded', 'Fraud', 'Other')")
    cursor.execute("""
        create table premium_users
        (
            patreon_id bigint not null constraint patreon_id_pk primary key,
            discord_id bigint,
            lifetime_support_cents int,
            last_charge_date date not null,
            last_charge_status premium_last_charge_status_enum not null,
            tokens int,
            tokens_spent int
        );
    """)


def down(cursor):
    cursor.execute("DROP TYPE guild_features_enum CASCADE")
    cursor.execute("DROP TABLE guild_features")
    cursor.execute("alter table guild_settings rename column nitro_role to announcement_channel")
    cursor.execute("alter table guild_settings drop column enable_pings")
    cursor.execute("DROP TYPE premium_last_charge_status_enum CASCADE")
    cursor.execute("DROP TABLE premium_users")
