# demns userbot
  my own userbot
  
  **гайд по юзерботу**
  
[Сперва открываем эту ссылку](https://my.telegram.org/auth)

потом скачиваем репозиторий, разархивируем.

потом открваем файл account.json

там где айди вводим ваш айди который получили [тут](https://my.telegram.org/auth)

ну и хеш там где хеш

потом запускаем main.py вводим свой номер, потом код... и всё!

префикс "-"

модули: help, dick, и exec (выполняет питоницческий код)

ПРИМЕЧАНИЕ: бот ну ооочень кривой, не обижайтесь.

**ГАЙД ПО МОДУЛЯМ:**

создаем <имямодуля>.py в папке /modules/

далее создаем метод start с тремя аргументами: message,mess,app

пример кода на модуле exec:

def start(message,mess,app):
    app.send_message(message.chat.id, "Выполняется питончиковый код: \n"+mess[1])
    exec(mess[1])
    
# мне лень девелопть это бота, если кто-то захочет то может быть да
