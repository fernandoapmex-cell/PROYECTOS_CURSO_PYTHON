class Biblioteca:
    def __init__(self,nombre:str):
        self._nombre = nombre
        self._libros=[ ]

    def agregar_libro(self,libro):
        self._libros.append(libro)

    def buscar_libros_autor(self,autor):
        for libro in self._libros:
            if libro.get_autor.lower() == autor.lower():
                self.mostrar_libro(libro)
    def buscar_libros_genero(self, genero):
        for libro in self._libros:
            if libro.get_genero.lower() == genero.lower():
                self.mostrar_libro(libro)
    def mostrar_todos_libros(self):
        print(f'\nTodos los libros de la biblioteca {self._nombre}')
        for libro in self._libros:
            self.mostrar_libro(libro)

    def mostrar_libro(self,libro):
        print(f'Libro-> Titulo:{libro.get_titulo}, Autor:{libro.get_autor},Genero:{libro.get_genero})')

    #Obtener nombre biblioteca
    @property
    def get_nombre(self):
        return self._nombre

    #obtener lista de libros
    @property
    def get_libros(self):
        return self._libros