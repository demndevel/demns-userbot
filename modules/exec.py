def start(message,mess,app):
    #...
    app.send_message(message.chat.id, "Выполняется питончиковый код: \n"+mess[1])
    exec(mess[1])