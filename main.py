import json
from pyrogram import Client
from pyrogram.handlers import MessageHandler
import os
import importlib

with open('account.json', 'r', encoding='utf-8') as f: 
    text = json.load(f) 
api = text["api"]
api_hash = text["hash"]
app = Client("account",api,api_hash)
modules = os.listdir(os.getcwd()+"/modules/")
with app:
    id = app.get_me()["id"]

def my_function(client, message):
    
    if id==message.from_user.id:
        if message.text[0] == "-":
            mess = message.text[1:].split(" ")
            for mm in modules:
                if mess[0] == mm[:-3]:
                    module = importlib.import_module("modules."+mm[:-3])
                    module.start(message,mess,app)
                    

my_handler = MessageHandler(my_function)
app.add_handler(my_handler)
app.run()  