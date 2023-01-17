import telebot

bot = telebot.TeleBot("Token")

# Lista de ID de contactos a los que se reenviarán los mensajes
contact_ids = []

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Bienvenido, a ChatAnonimo \n\n preciona \conectarme para resivir mensajes")

@bot.message_handler(commands=['chatid'])
def chaid(message):
    bot.send_message(message.chat.id, f"Tu chat ID es: {message.chat.id}")

@bot.message_handler(commands=['addchatid'])
def add_chat_id(message):
    new_ids = message.text.split()[1:]
    ids_valid = True
    for new_id in new_ids:
        if not new_id.isnumeric():
            ids_valid = False
    if ids_valid:
        contact_ids.extend(list(map(int, new_ids)))
        bot.send_message(message.chat.id, f"Los siguientes ID de chat agregados a la lista de reenvío: {new_ids}")
    else:
        bot.send_message(message.chat.id, "Formato de comando invalido, el comando debe ser '/addchatid [id_chat1] [id_chat2] ...'")

@bot.message_handler(commands=['conectame'])
def connect_me(message):
    if message.chat.id not in contact_ids:
        contact_ids.append(message.chat.id)
        bot.send_message(message.chat.id, "Tu ID de chat ha sido agregado a la lista de reenvío.")
    else:
        bot.send_message(message.chat.id, "Tu ID de chat ya está en la lista de reenvío.")

@bot.message_handler(content_types=['text','photo','video'])
def repeat_messages(message):
    for contact_id in contact_ids:
        bot.forward_message(contact_id, message.chat.id, message.message_id)
    if message.chat.id not in contact_ids:
        bot.send_message(message.chat.id, "✅ el Administrador lo a recivido.")

bot.delete_webhook()
bot.polling()

