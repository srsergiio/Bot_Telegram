import telebot

bot = telebot.TeleBot("token del bot")

# ID del contacto al que se reenviarán los mensajes
contact_id = #chatit entre la pesona y el bot donde se redirigira los mensajes

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Bienvenido, ahora puede enviar tus aportes anonimamente.")


@bot.message_handler(commands=['Aporte'])
def resend_history(message):
    # Obtener todos los mensajes en el historial del chat
    history = bot.get_chat_history(message.chat.id)
    for msg in history:
        # Reenviar cada mensaje a contact_id
        bot.forward_message(contact_id, message.chat.id, msg.message_id)

@bot.message_handler(commands=['chatid'])
def send_chat_id(message):
    bot.send_message(message.chat.id, f"El ID de este chat es: {message.chat.id}")
    bot.send_message(message.chat.id, "✅ el Administrador lo a recivido.")

@bot.message_handler(content_types=['text'])
def repeat_text_messages(message):
    bot.forward_message(contact_id, message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "✅ el Administrador lo a recivido.")

@bot.message_handler(content_types=['photo'])
def repeat_photo_messages(message):
    bot.forward_message(contact_id, message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "✅ el Administrador lo a recivido.")

@bot.message_handler(content_types=['video'])
def repeat_video_messages(message):
    bot.forward_message(contact_id, message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "✅ el Administrador lo a recivido.")

bot.delete_webhook()
bot.polling()