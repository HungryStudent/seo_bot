from keyboards import messengers
from utils.db import get_new_users
from create_bot import bot
import asyncio


async def main():
    data = await get_new_users()
    for user in data:
        try:
            await bot.send_message(user["user_id"],
                                   f"{user['first_name']}, поддерживай наш проект в социальных сетях и следи за самыми свежими новостями",
                                   reply_markup=messengers,
                                   parse_mode="HTML")
        except:
            pass
    session = await bot.get_session()
    await session.close()


asyncio.run(main())
