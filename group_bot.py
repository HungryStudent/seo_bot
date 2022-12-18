import asyncio

from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ContentTypes
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram import Bot

from utils.db import get_user
from config import sub_channel_id, GROUP_TOKEN, sub_channel_url, sub_bot_url, sub_text, sub_partner_url, sub_admins

bot = Bot(token=GROUP_TOKEN)
dp = Dispatcher(bot)

sub_kb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton("Канал 🚀", url=sub_channel_url),
                                               InlineKeyboardButton("Чат-бот 🤖", url=sub_bot_url),
                                               InlineKeyboardButton("Узнай на какой позиции твой товар",
                                                                    url=sub_partner_url))


async def on_startup(_):
    pass


@dp.message_handler(content_types=ContentTypes.NEW_CHAT_MEMBERS)
async def new_member(message: Message):
    pass


@dp.message_handler(content_types=ContentTypes.LEFT_CHAT_MEMBER)
async def new_member(message: Message):
    pass


@dp.message_handler(content_types=ContentTypes.ANY)
async def check_sub(message: Message):
    if message.from_user.id in sub_admins:
        return
    user = await get_user(message.from_user.id)
    sub_status = -1
    if user is None:
        sub_status += 1
    member = await message.bot.get_chat_member(sub_channel_id, message.from_user.id)
    if member.status not in ["member", "admin", "creator"]:
        sub_status += 1
    if sub_status == -1:
        return
    msg = await message.answer(sub_text.format(name=message.from_user.first_name),
                               reply_markup=sub_kb)
    await message.delete()
    await asyncio.sleep(300)
    await msg.delete()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
