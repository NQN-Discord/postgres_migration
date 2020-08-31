import os

cur_path = os.path.abspath(os.path.dirname(__file__))
migrations_directory = f"{cur_path}/sql/migrations"

# dbmigrator --migrations-directory=postgres_migration/sql/migrations --config=development.ini generate user_packs
