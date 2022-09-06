

import json
import requests
import time
from dbhelper import DBHelper
from datetime import date #Importar fecha



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

# Crea un json con los ultimos cambios
def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    js = get_json_from_url(url)
    return js



# guarda las nuevas actualizaciones en el archivo json creado en get_updates
def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)


# Control de actualizacion
def handle_updates(updates):
    for update in updates["result"]:
        try:
            text = update["message"]["text"]            #chat
            chat = update["message"]["chat"]["id"]      #id_chat
            etapas = db.get_etapas()

            user = db.select_user(chat)

            # guardar user en una  nueva variable utilizando la funcion fetchone()
            # por que al hacer print(user)  aparece "<sqlite3.Cursor object at 0x000001E707A92640>"
            userfetch = user.fetchone()

            if text != None:
                fecha = date.today() 
                db.add_log( fecha, text, chat)


            if text == "/my_id":
                 
                send_message("Tu id de telegram es:  "+str(chat), chat)



            if userfetch == None:
                send_message(
                    "Tu cuenta de telegram no se encuentra asignado a ningun usuario, tu ID de telegram es:  " + str(chat), chat)
            else:
                
                text, chat = get_last_chat_id_and_text(get_updates())

                tipo_notas              = ["entrada", "salida", "oportunidad"]
                     
                destruc_text            =   text.split()                                                    #destructucturacion ultimo mensaje por palabras
                
                id_etapa                =   db.get_id_etapas("Extraccion materia prima")                    #Guardo la id de la etapa "extraccion materia prima"
                id_etapa_diseño         =   db.get_id_etapas("Diseño y produccion")                         #Guardo la id de la etapa "Diseño y produccion"

                id_user                 =   db.get_id_user(chat)                                            #Guardo la id del user en la varible pero me la guarda como un objecto   
                id_userfetch            =   id_user.fetchone()                                              #destruyo el objecto y gyardo la id_user como un arreglo con un solo elemento            
                id_area                 =   db.get_id_area(id_userfetch[0])                                 #guardo la id del area llamando la funcion get_id_area(id_user) donde le entro el unico elemento del arreglo
                id_areafetch            =   id_area.fetchone()                                              #Al igual que la variable anterior este se guardo como un objeto y para romper le objeto utilizo fetchone()
                fecha                   = date.today()                                                      #Guardo al fecha  de hoy importantdo from datetime import date

                if text == "/start":
                    send_message("Como usar:\nIntrucciones de uso!!!!\n \nIngresa el comando:    /ingresar_datos\n \ninmediatamente se desplegara por pantalla todas las etapas disponibles.\nAl seleccionar una etapa se mostrara por pantalla la forma de ingresar tus notas, acompañado de ejemplos que facilitar tu uso del BOT.\nTe recomendamos seguir las instrucciones si es la primera vez que intereactuas con el BOT.\n \n----------------------------------- \n \nSi tu ya dominas el uso del bot puedes escribir rapidamente los siguentes comandos para ingresar tus notas:\n \nExtraccion materia prima:\n \next_entrada: 'tu nota'\next_salida: 'tu nota'\next_oportunidad: 'tu nota' ",chat)

                if text == "/estado_cuenta":
                    send_message(
                        "Tu ID de telegram se encuentra asignado a la cuenta con el Username:  " + str(userfetch), chat)
                
 
                if text == "/ingresar_datos":
                    keyboard = build_keyboard(etapas)
                    send_message("<b>Selecciona una etapa</b>", chat, keyboard)

                if text == "Extraccion materia prima": 
                    keyboard = keyboard_tipo_nota(tipo_notas)
                    send_message("Ingresa el tipo de nota", chat, keyboard  )
                    # send_message("Para ingresar una nota en extraccion de materia prima escribe lo siguente:", chat)
                    # send_message("Para registar una entrada:\next_entrada: 'tu nota'\n \nEJEMPLO: \next_entrada: harina\n------------------------------\n \n \nPara registrar una salida:\next_salida: 'tu nota'\n \nEJEMPLO: \next_salida: harina\n------------------------------\n \n \nPara registrar una oportunidad:\next_oportunidad: 'tu nota'\n \nEJEMPLO: \next_oportunidad: harina", chat)

                if text == "entrada extraccion":
                    send_message("Ingrese una entrada de la siguente forma\n \nEJEMPLO:\n \next_entrada: harina", chat)


                # extraccion    
                if destruc_text[0] == "ext_entrada:":  
                    db.add_entrada(destruc_text[1], id_etapa[0], id_userfetch[0], id_areafetch[0], fecha)
                    send_message("Tu entrada: "+ destruc_text[1]+ " ,se ha guardado en la base de datos", chat)

                if destruc_text[0] == "ext_salida:":  
                    db.add_salida(destruc_text[1], id_etapa[0], id_userfetch[0], id_areafetch[0], fecha)
                    send_message("Tu salida: "+ destruc_text[1]+ " ,se ha guardado en la base de datos", chat)
                
                if destruc_text[0] == "ext_oportunidad:":
                    db.add_oportunidad(destruc_text[1], id_etapa[0], id_userfetch[0], id_areafetch[0], fecha)
                    send_message("Tu Oportunidad: "+ destruc_text[1]+ " ,se ha guardado en la base de datos", chat)    

                #Diseño
                if destruc_text[0] == "dis_entrada:":  
                    db.add_entrada(destruc_text[1], id_etapa_diseño[0], id_userfetch[0], id_areafetch[0], fecha)
                    send_message("Tu entrada: "+ destruc_text[1]+ " ,se ha guardado en la base de datos", chat)

                if destruc_text[0] == "dis_salida:":  
                    db.add_salida(destruc_text[1], id_etapa_diseño[0], id_userfetch[0], id_areafetch[0], fecha)
                    send_message("Tu salida: "+ destruc_text[1]+ " ,se ha guardado en la base de datos", chat)
                
                if destruc_text[0] == "dis_oportunidad:":
                    db.add_oportunidad(destruc_text[1], id_etapa_diseño[0], id_userfetch[0], id_areafetch[0], fecha)
                    send_message("Tu Oportunidad: "+ destruc_text[1]+ " ,se ha guardado en la base de datos", chat)     
            
        except KeyError:
            pass




    


# guarda el ultimo mensaje
def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)



def build_keyboard(etapas):
    keyboard = [[etapa] for etapa in etapas]
    reply_markup = {"keyboard": keyboard, "one_time_Keyboard": True}
    return json.dumps(reply_markup)




def keyboard_tipo_nota(tipo_notas):
    keyboard = [[nota] for nota in tipo_notas]
    reply_markup = {"keyboard": keyboard, "one_time_Keyboard": True}
    return json.dumps(reply_markup)



# envia un nuevo mensaje
# repley_markup = build keyboard
def send_message(text, chat_id, reply_markup=None):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    if reply_markup:
        url += "&reply_markup={}".format(reply_markup)
    get_url(url)


def main():
    last_update_id = None  # creo una varible para guardar la id de la ultima actualizacion
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


# Definimos que si estamos en a main se ejecute la funcion main()
