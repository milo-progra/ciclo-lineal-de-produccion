

import json 
import requests
import time
from dbhelper import DBHelper




#TOKEN = "5356478941:AAF43swlSlBnsxBwMfBS2pl3gAM0l6yfGzY"
TOKEN = "5356478941:AAF43swlSlBnsxBwMfBS2pl3gAM0l6yfGzY"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
db = DBHelper() 


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js

#Crea un json con los ultimos cambios
def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    js = get_json_from_url(url)
    return js


#guarda las nuevas actualizaciones en el archivo json creado en get_updates
def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)


#Control de actualizacion 
def handle_updates(updates):
    for update in updates["result"]:
        try:
            text = update["message"]["text"]
            chat = update["message"]["chat"]["id"]

            user = db.select_user(chat)
            #guardar user en una  nueva variable utilizando la funcion fetchone()
            #por que al hacer print(user)  aparece "<sqlite3.Cursor object at 0x000001E707A92640>"
            userfetch = user.fetchone() 

            if text == "/my_id":
                    send_message("Tu id de telegram es:  "+str(chat), chat)

            if userfetch == None:
                send_message("Tu cuenta de telegram no se encuentra asignado a ningun usuario, tu ID de telegram es:  "+ str(chat), chat)
            else:
                if text == "/estado_cuenta":
                    send_message("Tu ID de telegram se encuentra asignado a la cuenta con el Username:  "+ str(userfetch), chat)

        except KeyError:
            pass


#guarda el ultimo mensaje 
def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


#envia un nuevo mensaje
def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)
    

def main():

    
    last_update_id = None #creo una varible para guardar la id de la ultima actualizacion
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            handle_updates(updates)
        time.sleep(0.5)    

if __name__ == '__main__':
    main()

# def main():
#     last_textchat = (None)
#     while True:
#         text, chat = get_last_chat_id_and_text(get_updates())
#         if (text, chat) != last_textchat:
#             send_message(text, chat)
#             last_textchat = (text, chat)
#         time.sleep(0.5)


#Definimos que si estamos en a main se ejecute la funcion main()

