from os import getenv


DATABASE_URL = getenv(
    "DATABASE_URL", "sqlite:///whereistheaccent/sql_app.db"
)
# DATABASE_URL = getenv(
#     "postgresql://user:password@postgresserver/db"
# )