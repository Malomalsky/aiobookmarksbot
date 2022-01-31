from aiogram import types
from aiogram.dispatcher.filters import IsReplyFilter
from environs import re
from bot.db.functions import add_bookmark_by_chat, find_bookmarks_by_chat_id, delete_bookmark
from bot.models.bookmarck_schema import BookmarkWithId
from loader import dp

LINK_TEMPLATE = '<a href="{0}">{1}</a>\n'

@dp.message_handler(IsReplyFilter(is_reply=True), commands=['save'])
async def save_bookmark(message: types.Message):
    description = message.get_args()
    if description:
        link = message.reply_to_message.url
        await add_bookmark_by_chat(message.chat, link, description)
        await message.answer("Записал!")
    else:
        await message.answer("Передайте описание вместе с командой.")


@dp.message_handler(IsReplyFilter(is_reply=True), commands=['delete'])
async def delete(message: types.Message):
    if await delete_bookmark(message): 
        await message.answer("Done.")
    else:
        await message.answer("Сообщение не было сохранено.")


@dp.message_handler(commands=['summary'])
async def summary(message: types.Message):
    bookmarks = await find_bookmarks_by_chat_id(message.chat)
    reply = ""
    for bookmark in bookmarks: 
        reply+= LINK_TEMPLATE.format(bookmark.link, bookmark.description)
    await message.answer(reply)
    


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(message.chat.id)
