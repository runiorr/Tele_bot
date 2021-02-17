from telegram.ext import Updater, CommandHandler


def welcome(update, context):
    firstname = update.message.from_user.first_name
    message = 'Olá, ' + str(firstname) + '!'
    print(message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def main():
    token = '1685254561:AAE6daoEvzd77vws0D_qBzO2Nx0azyq_aho'
    updater = Updater(token=token, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', welcome))
    
    updater.start_polling()
    print(str(updater))
    updater.idle()


if __name__ == "__main__":
    main()