from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca


class BibliotecaDAO:
    def __init__(self):
        pass

    def get_all_biblioteche(self):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            return result

        cursor = cnx.cursor(dictionary=True)
        query = "SELECT * FROM biblioteca"
        cursor.execute(query)

        for row in cursor:
            result.append(Biblioteca(**row))

        cursor.close()
        cnx.close()
        return result