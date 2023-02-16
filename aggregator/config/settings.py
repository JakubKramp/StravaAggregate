import environ

env = environ.Env()
environ.Env.read_env()
SQLALCHEMY_DATABASE_URI = f"postgresql://{env('POSTGRES_USER')}:{env('POSTGRES_PASSWORD')}@postgres/{env('POSTGRES_DATABASE')}"
