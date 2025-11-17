#diferencia entre variables de clase y de instancia(objeto)
class Perro:
    numero_patas = 4 #variable de clase

    def __init__(self,nombre):
        self.nombre = nombre #variable de instancia (del objeto)
    #definimos algunos objetos
layla= Perro('layla')
venus = Perro('venus')
#cada objeto tiene su propio atributo de nombre
print(layla.nombre,venus.nombre)
#la variable se puede accder con el nombre de la clase o con los objetos
print(layla.numero_patas,venus.numero_patas , Perro.numero_patas)
#si tratamos de accder la variable de instancia desde la clase no es posible
#print(Perro.nombre)
#si queremos modificar el numero de patas para todos los perros
Perro.numero_patas = 5
print(layla.numero_patas,venus.numero_patas , Perro.numero_patas)
#si queremos modificar el numero de patas para solo un perro
venus.numero_patas = 2# aqui ocurre un detalle
print(layla.numero_patas,venus.numero_patas , Perro.numero_patas)
#imprimimos el valor de la variable de instancia y ademas la de clase
print(venus.numero_patas,venus.__class__.numero_patas)
#Si creamos una variable desde la clase
Perro.nombre = 'Clase Perro'
print(layla.nombre,venus.nombre,Perro.nombre)

#si definimos una variable de clase que no esta en los objetos
Perro.numero_orejas = 2
print(layla.numero_orejas,venus.numero_orejas,Perro.numero_orejas)
#implementacion erronea
class ContadorObjetosErronea:
    numero_instancias  = 0
    def __init__(self):
        #Aca esta el error
        self.__class__.numero_instancias += 1
print(f'Contador instancias erroneo: {ContadorObjetosErronea.numero_instancias}')
objeto=ContadorObjetosErronea()
objeto2 = ContadorObjetosErronea()
objeto2 = ContadorObjetosErronea()
objeto2 = ContadorObjetosErronea()
objeto2 = ContadorObjetosErronea()
print(ContadorObjetosErronea.numero_instancias)
