import requests

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url

def get_dog_photo(update, context):
    url = get_url()
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=url)



def welcome(update, context):
    firstname = update.message.from_user.first_name
    message = 'Olá, ' + str(firstname) + '!'
    print(message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)



