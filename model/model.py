from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO

class Model:
    def __init__(self):
        self._biblioteca_dao = BibliotecaDAO()
        self._libro_dao = LibroDAO()

    def get_libri_filtrati(self, biblioteca: str, genere: str):
        return self._libro_dao.get_libri_filtrati(biblioteca, genere)

    def get_generi(self):
        return self._libro_dao.get_generi()

    def get_biblioteche(self):
        return self._biblioteca_dao.get_all_biblioteche()