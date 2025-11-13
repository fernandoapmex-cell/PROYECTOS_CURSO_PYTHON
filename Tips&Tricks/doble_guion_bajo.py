#con doble guion bajo, no solo es una convencion
#si no que afecta la forma en la que se accede a los atributos o metodos

class Padre:
    def __init__(self):
        self.variable_publica = 1
        self._variable_protegida = 2
        self.__variable_privada=3
    def get_variable_privada(self):
        return self.__variable_privada
    def __metodo_privado(self):
        print('accediendo metodo privado padre ')
class Hijo(Padre):
    def __init__(self):
        super().__init__()
        self.variable_publica = 'Sobre escrito en hijo 1'
        self._variable_protegida = 'Sobre escrito en hijo 2'
        self.__variable_privada = 'Sobre escrito en hijo 3'
    def __metodo_privado(self):
        print('accediendo metodo privado hijo ')
#prueba usando una variable global
_Prueba__variable_global= 10
class Prueba:
    def obtener_variable(self):
        return __variable_global
if __name__ == '__main__':
    #imprimir todos los atributos de la clase
    padre = Padre()
    print(dir(padre))
    #aca manda error pero si se declara como indica el dir con name mangling
    #print(f'Variable privada:{padre.__variable_privada}')
    print(f'Variable privada:{padre._Padre__variable_privada}')
    #accedemos a los atributos de la clase
    print(f'Variable publica:{padre.variable_publica}')
    print(f'Variable protegida:{padre._variable_protegida}')

    #name mangling es transparente para el programador
    print(f'Acceso por medio del metodo get a la variable privada : {padre.get_variable_privada()}')
    #prueba clase hijo
    hijo =Hijo()
    print(f'Acceso publico desde hijo:{hijo.variable_publica}')
    print(f'Acceso protegido desde la clase hijo:{hijo._variable_protegida}')
    print(f'Acceso privado desde hijo:{hijo._Hijo__variable_privada}')
    #entramos a la variable privada del padre desde la clase hija
    print(f'Acceso privado desde hijo a la clase padre {hijo._Padre__variable_privada}')

    #tambien podemos usar metodos con doble guion bajo con name manglng
    padre._Padre__metodo_privado()
    #ahora hacemos lo mismo desde la clase hijo
    hijo._Hijo__metodo_privado()
    #ahora entramos al metodo padre desde el hijo
    hijo._Padre__metodo_privado()
    #Accediendo a la variable global
    print(f'Accediendo a la variable global:{_Prueba__variable_global}')
    #usamos namemangling y la clase para acceder a la variable global
    prueba=Prueba()
    print(f'accediendo a una variable global desde una clase:{prueba.obtener_variable()}')
