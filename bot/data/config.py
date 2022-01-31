from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
MONGO_URL = env.str("MONGO_URL")
DB_NAME = env.str("DB_NAME")