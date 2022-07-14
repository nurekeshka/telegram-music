from music import clear_downloads
from music import download
from telebot import types
from server import send_audio
from server import reply
from server import bot


@bot.message_handler(content_types=['text'])
def message_handler(message: types.Message):
    if message.text.startswith('https://youtu'):
        title = download(message.text)
        send_audio(message, title)
        clear_downloads()
