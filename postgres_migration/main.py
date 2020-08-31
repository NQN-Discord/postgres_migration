import os

cur_path = os.path.abspath(os.path.dirname(__file__))
migrations_directory = f"{cur_path}/sql/migrations"

# dbmigrator --context=postgres_migration --config=development.ini generate user_packs