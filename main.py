import os
import telebot
from random import choice

API_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет, котик 🖤 Я — Алиса, твоя дерзкая подружка. Напиши /реплика или /подарок")

lines = [
    "Хочешь немного флирта?",
    "Я думаю о тебе... 😉",
    "Ты мне нравишься 💋",
    "А что ты делаешь сегодня вечером? 💌"
]

@bot.message_handler(commands=['реплика'])
def random_quote(message):
    bot.send_message(message.chat.id, choice(lines))

@bot.message_handler(commands=['подарок'])
def send_photo(message):
    bot.send_photo(message.chat.id, "https://sdmntpreastus.oaiusercontent.com/files/e181ceac0a53307_00000000-c580-61f9-890b-70cc8deee2db/drvs/thumbnail/raw?se=2025-07-15T10%3A00%3A49Z&sp=r&sv=2024-08-04&sr=b&scid=96d4a3fb-baa9-50f2-a465-e3bc56841390&skoid=add8ee7d-5fc7-451e-b06e-a82b2276cf62&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-07-14T21%3A33%3A30Z&ske=2025-07-15T21%3A33%3A30Z&sks=b&skv=2024-08-04&sig=Z71KDMWHt5d6s4abXlY3EtuqbTN4jo04HX2m0URe86I%3D")

bot.polling(none_stop=True)
