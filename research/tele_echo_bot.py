import logging
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os,sys

load_dotenv()

API_TOKEN = os.getenv("TOKEN")
# print(API_TOKEN)


# Configure Logging
logging.basicConfig(level=logging.INFO)


# Initialize Bot and Dispathcer
bot = Bot(API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands = ['start','help'])
async def command_start_handler(message : types.Message) -> None:
    """ 
    This handler receives   messages with '\start' or '\help' command
    """

    await message.reply("HII\nI am en Echo Bot!\nPowered by aiogram.")



@dp.message_handler()
async def echo(message : types.Message) -> None:
    """ 
    This will return echo
    """

    await message.answer(message.text)



if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)