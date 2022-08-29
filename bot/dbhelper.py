from distutils.util import execute
import sqlite3

class DBHelper:
    
    def __init__(self):
        self.conn = sqlite3.connect("cicloProduccion/db.sqlite3")

    
    def select_user(self, id_telegram):
        stmt = "SELECT username FROM user_usuario WHERE id_telegram = (?)"
        args = (id_telegram, )
        return self.conn.execute(stmt, args)