import requests
import my_infos
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                         RegexHandler, ConversationHandler)
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove


def welcome(update, context):
    firstname = update.message.from_user.first_name
    message = 'Olá, ' + str(firstname) + '!'
    print(message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url

def get_dog(update, context):
    url = get_url()
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=url)


def main():
    token = my_infos.token
    updater = Updater(token=token, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', welcome))
    updater.dispatcher.add_handler(CommandHandler('dog', get_dog))

    
    updater.start_polling()
    print(str(updater))
    updater.idle()


if __name__ == "__main__":
    main()