import os


temp_folder = os.path.join(os.path.dirname(__file__), 'temp')

if not os.path.exists(temp_folder):
    os.mkdir(temp_folder)
