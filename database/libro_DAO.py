from database.DB_connect import DBConnect
from model.libro_DTO import Libro


class LibroDAO:
    def __init__(self):
        pass

    def get_generi(self):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            return result

        cursor = cnx.cursor(dictionary=True)
        query = "SELECT DISTINCT genere FROM libro WHERE genere IS NOT NULL"
        cursor.execute(query)

        for row in cursor:
            result.append(row["genere"])

        cursor.close()
        cnx.close()
        return result

    def get_libri_filtrati(self, nome_biblioteca, genere):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            return result

        cursor = cnx.cursor(dictionary=True)
        query = """
            SELECT l.* 
            FROM libro l
            JOIN biblioteca b ON l.id_biblioteca = b.id_biblioteca
            WHERE b.nome = COALESCE(%s, b.nome)
              AND l.genere = COALESCE(%s, l.genere)
        """
        cursor.execute(query, (nome_biblioteca, genere))

        for row in cursor:
            result.append(Libro(**row))

        cursor.close()
        cnx.close()
        return result