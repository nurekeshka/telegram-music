import configparser


config = configparser.ConfigParser()
config.read('./settings.ini')
TOKEN = config.get('DEFAULT', 'TOKEN')
