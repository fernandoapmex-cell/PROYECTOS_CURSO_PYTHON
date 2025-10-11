class Cliente:
    def __init__(self,id_cliente=None, nombre_cliente=None, apellido_cliente=None,membresia_cliente=None):
        self._id_cliente=id_cliente
        self._nombre_cliente=nombre_cliente
        self._apellido_cliente=apellido_cliente
        self._membresia_cliente=membresia_cliente

    def __str__(self):
        return f'Id Cliente: {self._id_cliente},Nombre Cliente:{self._nombre_cliente},Apellido Cliente:{self._apellido_cliente},Membresia Cliente:{self._membresia_cliente}'

    @property
    def id_cliente(self):
        return self._id_cliente
    @id_cliente.setter
    def id_cliente(self,id_cliente):
        self._id_cliente=id_cliente
    @property
    def nombre_cliente(self):
        return self._nombre_cliente
    @nombre_cliente.setter
    def nombre_cliente(self,nombre_cliente):
        self._nombre_cliente=nombre_cliente
    @property
    def apellido_cliente(self):
        return self._apellido_cliente
    @apellido_cliente.setter
    def apellido_cliente(self,apellido_cliente):
        self._apellido_cliente=apellido_cliente
    @property
    def membresia_cliente(self):
        return self._membresia_cliente
    @membresia_cliente.setter
    def membresia_cliente(self,membresia_cliente):
        self._membresia_cliente=membresia_cliente

