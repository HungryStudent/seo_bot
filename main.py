from aiogram.utils import executor
from handlers import users
from create_bot import dp
from utils.db import start_db


async def on_startup(_):
    await start_db()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
