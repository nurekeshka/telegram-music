from constants import temp_folder
from server import send_audio
from telebot import types
import os


def clear_downloads():
    for file in os.listdir(temp_folder):
        os.remove(os.path.join(temp_folder, file))


def download_callback(message: types.Message, file_path: str):
    clear_downloads()
    send_audio(message, file_path)
