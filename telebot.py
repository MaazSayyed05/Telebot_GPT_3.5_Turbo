import os,sys
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
import openai,requests

class Reference:
    """
    A class to store previosly response from ChatGPT API
    """

    def __init__(self) -> None:
        self.response = ""



load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

reference = Reference()

BOT_TOKEN = os.getenv("TOKEN")

# Model NAme
MODEL_NAME = 'gpt-3.5-turbo'


# Initialize Bot and Dispathcer
bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)


def clear_past():
    """
    A function to forget/clear previious context and conversation

    """
    reference.response = ""



@dp.message_handler(commands = ['start','help'])
async def welcome   (message : types.Message) -> None:
    """ 
    This handler receives   messages with '\start' or '\help' command
    """

    await message.reply("HII\nI am en Tele Bot!\Created by Maaz.How can I assist you?")



@dp.message_handler(commands=['clear'])     
async def clear(message: types.Message):
    """
    A handler to clear the previosus conversations and context
    """

    clear_past()

    await message.reply("I've cleared the past conversation and context.")


@dp.message_handler(commands=['help'])
async def helper(message: types.Message):
    """
    A handler to display the help menu.
    """
    help_command = """
    Hi There, I'm chatGPT Telegram bot created by Bappy! Please follow these commands - 
    /start - to start the conversation
    /clear - to clear the past conversation and context.
    /help - to get this help menu.
    I hope this helps. :)
    """
    await message.reply(help_command)



@dp.message_handler()
async def chatgpt(message: types.Message):
    """
    A handler to process the user's input and generate a response using the chatGPT API.
    """
    print(f">>> USER: \n\t{message.text}")
    response = openai.ChatCompletion.create(
        model = MODEL_NAME,
        messages = [
            {"role": "assistant", "content": reference.response}, # role assistant
            {"role": "user", "content": message.text} #our query 
        ]
    )
    reference.response = response['choices'][0]['message']['content']
    print(f">>> chatGPT: \n\t{reference.response}")
    await bot.send_message(chat_id = message.chat.id, text = reference.response)




if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)



