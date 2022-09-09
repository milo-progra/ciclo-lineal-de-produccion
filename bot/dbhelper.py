from distutils.util import execute
import sqlite3

class DBHelper:
    #funcion para encontrar la base de datos en pythonenywhere.com
    # def __init__(self):
    #     self.conn = sqlite3.connect("/home/miloVan/ciclo-lineal-de-produccion/db.sqlite3")
    
    def __init__(self):
        self.conn = sqlite3.connect("cicloProduccion/db.sqlite3")

    
    def select_user(self, id_telegram):
        stmt = "SELECT username FROM user_usuario WHERE id_telegram = (?)"
        args = (id_telegram, )
        return self.conn.execute(stmt, args)

    def get_id_user(self, id_telegram):
        stmt = "SELECT id FROM user_usuario WHERE id_telegram = (?)"
        args = (id_telegram, )
        return self.conn.execute(stmt, args)    

    def get_etapas(self):
            stmt = "SELECT nombre FROM app_etapa"
            return[x[0] for x in self.conn.execute(stmt)]

    def get_id_etapas(self, nombre_etapa ):
        stmt = "SELECT id_etapa FROM app_etapa WHERE nombre = (?)"
        args = (nombre_etapa, )
        return[x[0] for x in self.conn.execute(stmt, args)]

    def get_id_area(self, id_usuario_id):
        stmt = "SELECT id_area_id FROM app_registrotrabajador WHERE usuario_id = (?)"
        args = (id_usuario_id, ) 
        return self.conn.execute(stmt, args)       


    def add_entrada(self, nota, etapa_id, usuario, id_area, fecha ):
        stmt = "INSERT INTO app_entrada (nombre, etapa_id, usuario_id, id_area_id, fecha) VALUES (?, ? , ?, ?, ?)"   
        args = (nota, etapa_id, usuario, id_area, fecha)
        self.conn.execute(stmt, args)
        self.conn.commit()

    def add_salida(self, nota, etapa_id, usuario, id_area, fecha ):
        stmt = "INSERT INTO app_salida (nombre, etapa_id, usuario_id, id_area_id, fecha) VALUES (?, ? , ?, ?, ?)"   
        args = (nota, etapa_id, usuario, id_area, fecha)
        self.conn.execute(stmt, args)
        self.conn.commit()

    def add_oportunidad(self, nota, etapa_id, usuario, id_area, fecha ):
        stmt = "INSERT INTO app_oportunidades (nombre, etapa_id, usuario_id, id_area_id, fecha) VALUES (?, ? , ?, ?, ?)"   
        args = (nota, etapa_id, usuario, id_area, fecha)
        self.conn.execute(stmt, args)
        self.conn.commit()


    def add_log(self, fecha, text, id_telegram):
        stmt = "INSERT INTO administrador_logtelegram (timesstap, text, id_telegram) VALUES (?, ?, ?)"
        args = (fecha, text, id_telegram)
        self.conn.execute(stmt, args)
        self.conn.commit()  