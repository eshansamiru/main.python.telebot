import os
import telebot

bot = telebot.TeleBot("5149814890:AAEygWwKAZU9MY_6DdUixgs527k8fYJqpb8")

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message,"Hello! I am Chat BOT")

@bot.message_handler(commands=["how"])
def send_welcome(message):
    bot.reply_to(message,"https://t.me/Anytime_Sri_Lankan_link_Share")

@bot.message_handler(commands=["wallpapers"])
def send_welcome(message):
    bot.reply_to(message, "https://images.app.goo.gl/khqJQhHS294z3zxu8")

@bot.message_handler(commands=["telegrampc"])
def send_welcome(message):
    bot.reply_to(message, "https://telegram.org/dl/desktop/win64")

@bot.message_handler(commands=["beautiful"])
def send_welcome(message):
    bot.reply_to(message, "https://cdn.wallpapersafari.com/25/30/4oXdAe.jpg")

bot.polling()
