from setuptools import setup

setup(
    name="postgres_migration",
    version="0.1.0",
    description="Migrate NQN's postgres db",
    author='Blue',
    url="https://nqn.blue/",
    packages=["postgres_migration"],
    entry_points={
        "dbmigrator": [
            "migrations_directory = main:migrations_directory",
        ],
    },
)
