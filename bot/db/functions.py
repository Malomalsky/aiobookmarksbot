import asyncio

from aiogram.types import Chat, Message
from environs import re
from motor.motor_asyncio import AsyncIOMotorDatabase

from bot.models.bookmarck_schema import Bookmark, BookmarkWithId
from loader import db_connection


def _dispatch_chat_id(chat: Chat) -> AsyncIOMotorDatabase:
    chat_id = str(chat.id)
    return db_connection[chat_id]


async def add_bookmark_by_chat(chat: Chat, url: str, description: str) -> None:
    chat_collection = _dispatch_chat_id(chat)
    bookmark = Bookmark(link=url, description=description)
    await chat_collection.insert_one(bookmark.dict())


async def find_bookmarks_by_chat_id(chat: Chat) -> list[BookmarkWithId]:
    chat_collection = _dispatch_chat_id(chat)
    cursor = await chat_collection.find().to_list(length=200)
    return [BookmarkWithId(**document) for document in cursor]


async def delete_bookmark(message: Message) -> bool:
    chat_collection = _dispatch_chat_id(message.chat)
    bookmark_link = message.reply_to_message.url
    result = await chat_collection.delete_one({'link': bookmark_link})
    return bool(result)

