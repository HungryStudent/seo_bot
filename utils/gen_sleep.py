import asyncio

from aiogram.types import Message, ChatActions


async def gen_sleep(message: Message, seconds: int):
    for i in range(seconds // 5):
        await message.answer_chat_action(ChatActions.TYPING)
        await asyncio.sleep(5)
