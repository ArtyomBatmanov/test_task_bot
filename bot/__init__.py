from .config import API_TOKEN
from .handlers import register_handlers
import telebot


def create_bot():

    bot = telebot.TeleBot(API_TOKEN)
    register_handlers(bot)
    return bot
