from aiogram.contrib.fsm_storage.memory import MemoryStorage
from decouple import config
from aiogram import Bot,Dispatcher

storage = MemoryStorage()
TOKEN = config("TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
GROUP_ID = [-4032820575, ]

DESTINATION = "C:/Users/acer/PycharmProjects/choposhssbot/media"