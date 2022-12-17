from aiogram.dispatcher import Dispatcher
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ContentTypes
from aiogram.utils import executor
from aiogram import Bot
from utils.db import get_user

TOKEN = "5958619383:AAHzvScq3PloVv18sbYMicEj_QPUqSAS09E"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

channel_id = -1001663696156

sub_text = ["{name}, подпишись на бота", "{name}, подпишись на канал", "{name}, подпишись на канал и бота"]
sub_kb = [InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton("Бот", url="https://t.me/efanov_dev_bot")),
          InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton("Канал", url="https://t.me/topkanalefan")),
          InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton("Бот", url="https://t.me/efanov_dev_bot"),
                                                InlineKeyboardButton("Канал", url="https://t.me/topkanalefan"))]


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
        sub_status += 2
    if sub_status == -1:
        return
    await message.answer(sub_text[sub_status].format(name=message.from_user.first_name),
                         reply_markup=sub_kb[sub_status])
    await message.delete()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
