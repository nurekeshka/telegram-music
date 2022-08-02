from telebot import TeleBot
from config import TOKEN


bot = TeleBot(token=TOKEN, threaded=True)


def send_audio(chat_id: int, file_path: str):
    with open(file_path, 'rb') as audio:
        bot.send_audio(
            chat_id=chat_id,
            audio=audio,
            timeout=60
        )
