import requests
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                         RegexHandler, ConversationHandler)
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove


STATE1 = 1
STATE2 = 2

def welcome(update, context):
    firstname = update.message.from_user.first_name
    message = 'Olá, ' + str(firstname) + '!'
    print(message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def feedback(update, context):
    message = 'Por favor, digite um feedback para o nosso tutorial:'
    update.message.reply_text(message, reply_markup=ReplyKeyboardMarkup([], one_time_keyboard=True)) 
    return STATE1

def inputFeedback(update, context):
    feedback = update.message.text
    print(feedback)
    if len(feedback) < 10:
        message = """Seu feedback foi muito curtinho... 
                        \nInforma mais pra gente, por favor?"""
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return STATE1
    else:
        message = "Muito obrigada pelo seu feedback!"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def inputFeedback2(update, context):
    feedback = update.message.text
    message = "Muito obrigada pelo seu feedback!"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def cancel(update, context):
    return ConversationHandler.END

def main():
    token = '1685254561:AAE6daoEvzd77vws0D_qBzO2Nx0azyq_aho'
    updater = Updater(token=token, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', welcome))

    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('feedback', feedback)],
        states={
            STATE1: [MessageHandler(Filters.text, inputFeedback)],
            STATE2: [MessageHandler(Filters.text, inputFeedback2)]
        },
        fallbacks=[CommandHandler('cancel', cancel)])
    updater.dispatcher.add_handler(conversation_handler)
    
    updater.start_polling()
    print(str(updater))
    updater.idle()


if __name__ == "__main__":
    main()