class Usuario:
    def __init__(self, id_usuario=None,nombre_usuario=None,password_usuario = None):
        self._id_usuario = id_usuario
        self._nombre_usuario = nombre_usuario
        self._password_usuario = password_usuario

    def __str__(self):
        return f'Usuario:{self._id_usuario} - Nombre:{self._nombre_usuario} - Password:{self._password_usuario}'

    @property
    def id_usuario(self):
        return self._id_usuario
    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self._id_usuario = id_usuario
    @property
    def nombre_usuario(self):
        return self._nombre_usuario
    @nombre_usuario.setter
    def nombre_usuario(self, nombre_usuario):
        self._nombre_usuario = nombre_usuario
    @property
    def password_usuario(self):
        return self._password_usuario
    @password_usuario.setter
    def password_usuario(self, password_usuario):
        self._password_usuario = password_usuario
