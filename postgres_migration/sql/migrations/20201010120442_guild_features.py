def up(cursor):
    cursor.execute("CREATE TYPE guild_features_enum AS ENUM ('emote_roles')")
    cursor.execute(
        """
        create table guild_features
        (
            guild_id bigint not null,
            feature guild_features_enum not null
        );
        """
    )
    cursor.execute("create index guild_features_feature_index on guild_features (feature)")
    cursor.execute("create index guild_features_guild_id_index on guild_features (guild_id)")


def down(cursor):
    cursor.execute("DROP TYPE guild_features_enum AS ENUM ('emote_roles')")
    cursor.execute("DROP TABLE guild_features")
