import telebot
from telebot import types
with open('tele_token.txt', 'r') as f:
    token = f.read().strip()
bot = telebot.TeleBot(token)
bot_creator = "@IMYdev"
