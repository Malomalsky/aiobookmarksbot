from aiogram import Bot, Dispatcher, types
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from bot.data.config import MONGO_URL, DB_NAME, BOT_TOKEN


def _connect_to_db() -> AsyncIOMotorDatabase:
    """Connecting to db with chats.

    Returns:
        AsyncIOMotorDatabase: Mongo database
    """
    client = AsyncIOMotorClient(MONGO_URL, io_loop=io_loop)
    client.get_io_loop = asyncio.get_running_loop
    db = client[DB_NAME]
    return db

io_loop = asyncio.get_event_loop()

db_connection = _connect_to_db()

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot=bot)