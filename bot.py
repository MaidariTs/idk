from aiogram import executor
from dispatcher import dp
from db import BotDB
from config import DATABASE


BotDB = BotDB(DATABASE)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
