import os

cur_path = os.path.abspath(os.path.dirname(__file__))
migrations_directory = f"{cur_path}/sql/migrations"

# dbmigrator --migrations-directory=postgres_migration/sql/migrations --config=development.ini generate user_packs
# dbmigrator --migrations-directory=/usr/local/lib/python3.6/site-packages/postgres_migration/sql/migrations --db-connection-string="user=postgres password=postgres host=postgres" list