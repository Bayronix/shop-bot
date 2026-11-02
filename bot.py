import asyncio
import os
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Привіт, це Демо")

@dp.message(Command("help")) 
async def help_command(message: Message):
    await message.answer("Біжу, біжу бро")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
   asyncio.run(main())