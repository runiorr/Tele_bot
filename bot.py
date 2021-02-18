from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                         RegexHandler, ConversationHandler)
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

import my_infos
import function


def main():
    token = my_infos.token
    updater = Updater(token=token, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', function.welcome))
    updater.dispatcher.add_handler(CommandHandler('dog', function.get_dog_photo))

    
    updater.start_polling()
    print(str(updater))
    updater.idle()


if __name__ == "__main__":
    main()