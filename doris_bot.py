import telebot

TOKEN = "5633537059:AAHFrFbPVzvdUyorVBvYZo6v3ng9EXzPdPk"

doris_bot = telebot.TeleBot(TOKEN)


@doris_bot.message_handler(commands=["1"])
def bedroom(message):
    doris_bot.send_message(message.chat.id, "Certo, já estou a caminho do seu quarto!")
    #send position bedroom

@doris_bot.message_handler(commands=["2"])
def room(message):
    doris_bot.send_message(message.chat.id, "Certo, já estou a caminho da sala de estar")
    #send position room

@doris_bot.message_handler(commands=["3"])
def bathroom(message):
    doris_bot.send_message(message.chat.id, "Certo, já estou a caminho do banheiro!")
    #send position bathroom 


def verify(message):
    return True

@doris_bot.message_handler(func=verify)
def answer(message):
    first_text = """
    Olá, eu sou a DoRIS! Me diga onde você está para que eu possa ajudar você. 
     /1 Estou no quarto.
     /2 Estou na sala de estar.
     /3 Estou no banheiro.
    """
    doris_bot.reply_to(message, first_text)

doris_bot.polling()
