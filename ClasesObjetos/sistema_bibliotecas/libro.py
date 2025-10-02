class Libro:
    def __init__(self,titulo:str, autor:str, genero:str):
        self._titulo = titulo
        self._autor = autor
        self._genero = genero

    @property
    def get_titulo(self):
        return self._titulo
    @property
    def get_autor(self):
        return self._autor
    @property
    def get_genero(self):
        return self._genero

