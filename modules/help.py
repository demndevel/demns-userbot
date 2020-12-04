from time import sleep
import os
import importlib 
import json
about = "Этот модуль отображает все доступные команды"
def start(message,mess,app):
    message.edit("хелпирую...")
    sleep(1)
    modules = os.listdir(os.getcwd()+"/modules/")
    mu = ""
    modules[-1]=""
    for m in modules:
        mu = mu+m+"\n"
        mu = mu[:-2]
        #mu+=modjson[m.replace(".py","")]
    message.edit("Список доступных **модулей** в **demn's telegram userbot**: \n "+mu,parse_mode="markdown")
