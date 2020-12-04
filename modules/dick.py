from time import sleep as s
def start(message,mess,app):
    message.edit("Дикую.  .  .")
    s(1)
    app.delete_messages(
    chat_id=message.chat.id,
    message_ids=message.message_id
    )
    app.send_message(message.chat.id, "/dick")
