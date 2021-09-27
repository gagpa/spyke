from . import from_env

DB_HOST = from_env('DB_HOST')
DB_PORT = from_env('DB_PORT')
DB_USER = from_env('DB_USER')
DB_PASS = from_env('DB_PASS')
DB_NAME = from_env('DB_NAME')
if DB_PORT:
    DB_URL = f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
else:
    DB_URL = f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}'
