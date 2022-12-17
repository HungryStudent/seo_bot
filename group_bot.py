from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ContentTypes
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram import Bot

from utils.db import get_user
from config import channel_id, GROUP_TOKEN

bot = Bot(token=GROUP_TOKEN)
dp = Dispatcher(bot)

sub_text = "Привет, {name}\n\nЧтобы писать в этой группе подпишитесь на наши канал и чат-бот"
sub_kb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton("Канал 🚀", url="https://t.me/WB_Services_Up_Bot"),
                                               InlineKeyboardButton("Чат-бот 🤖", url="https://t.me/SEO_for_WB"))


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
    user = await get_user(message.from_user.id)
    sub_status = -1
    if user is None:
        sub_status += 1
    member = await message.bot.get_chat_member(channel_id, message.from_user.id)
    if member.status not in ["member", "admin", "creator"]:
        sub_status += 1
    if sub_status == -1:
        return
    await message.answer(sub_text.format(name=message.from_user.first_name),
                         reply_markup=sub_kb)
    await message.delete()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
