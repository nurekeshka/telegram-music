from telebot import TeleBot
from telebot import types
from config import TOKEN
from music import temp_folder
import os


bot = TeleBot(token=TOKEN, threaded=True)


def send_audio(message: types.Message, filename: str):
    with open(os.path.join(temp_folder, f'{filename}.webm'), 'rb') as audio:
        bot.send_audio(
            chat_id=message.chat.id,
            audio=audio,
            timeout=60
        )
