from mi_modulo import funcion_publica,_funcion_protegida
#para usar funciones protegidas se tienen que declrar no usando *
class MiClase:
    def __init__(self):
        self.mi_variable_publica = 10
        self._mi_variable_protegida = 11


#el guion bajo al final se usa para evitar conflictos con nombres keywords
#ejmp class def etc
def funcion1(nombre,class_):
    print('funcion q recibe una clase')
#creamos la prueba de la clase
if __name__ == '__main__':
    objecto = MiClase()
    print(objecto.mi_variable_publica)
    #no deberiamos acceder atributos o metodos con un guion bajo al inicio en la practica
    print(objecto._mi_variable_protegida)

    #accedemos a las funciones del modulo importado
    funcion_publica()
    _funcion_protegida()
    funcion1('Juan',None)