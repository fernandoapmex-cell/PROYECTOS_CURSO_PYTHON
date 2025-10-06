class ManejoArchivos:
    def __init__(self,nombre):
        self.nombre = nombre
    def __enter__(self):
        print('entrando al recurso'.center(50,'-'))
        print(self.nombre)
        self.nombre = open(self.nombre,'r',encoding='utf-8')
        return self.nombre
    def __exit__(self,tipo_exception,valor_exception,traza_error):
        print('Cerreamos el recurso'.center(50,'-'))
        if self.nombre:
            self.nombre.close()
