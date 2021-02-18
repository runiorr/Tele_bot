import requests
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                         RegexHandler, ConversationHandler)
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Location


def get_lat_lon(update, context):
    lat = update.location.latitude
    lon = update.locaiton.longitude
    contents = requests.get('api.openweathermap.org/data/2.5/weather?lat={%la}&lon={%lo}&appid={cc0958870c407d46638e377805c68a32}' % (lat , lon)).json()
    weather = contents['lang']
    context.bot.send_message(chat_id=update.effective_chat.id, text=weather)
