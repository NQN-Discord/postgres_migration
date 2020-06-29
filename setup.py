from setuptools import setup, find_packages

setup(
    name="postgres_migration",
    version="0.1.0",
    description="Migrate NQN's postgres db",
    author='Blue',
    url="https://nqn.blue/",
    packages=find_packages(),
    entry_points={
        "dbmigrator": [
            "migrations_directory = main:migrations_directory",
        ],
    },
)
