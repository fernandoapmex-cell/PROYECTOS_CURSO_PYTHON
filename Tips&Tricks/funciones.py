#las funciones en py son ciudadanos de primera clase
def mayusculas(texto):
    return texto.upper()

#uso normal de la funcion
print(mayusculas('hola'))

#uso de una funcion como un objeto
#asignar la referencia de una funcion a una variable
variable_funcion = mayusculas
print(variable_funcion)
#utilizamos la variable funcion en cualquier momento
print(variable_funcion('nuevo texto'))

#para demostrar que las funciones son objetos ,eliminamos la referencia original
#del mayusculas
print(variable_funcion)
#podemos saber el nombre por default que se le asigna a una funcion} como ya la eliminamos no se puede usar pero si da el nombre que tuvo por default
print(f'Nombre por default de la funcion: {variable_funcion.__name__}')

#como almacenar una funcion en una estrucutra de datos
lista_funciones=[mayusculas, variable_funcion,str.upper]
print(lista_funciones)
#accder a cada una de las funciones
for funcion in lista_funciones:
    print(funcion,funcion('prueba con for ejecucion de funcion '))
#accedemos a la segunda funcion y la ejecutamos
print(lista_funciones[1]('saludos desde variable funcion'))

#pasar una funcion a otra funcion se llaman funciones de alto orden o high order

def saludar(argumento_funcion):
    #usamos la funcion que recibimos como argumento y devolvemos la referencia de esta funcion
    referencia_funcion_retoranda = argumento_funcion('Hola,saludos desde mi funcion')
    return print(referencia_funcion_retoranda)

#llamamos la funcion saludar ,pasamos la referencia de una funcion como argumento
saludar(mayusculas)

#podemos pasar una neuva implementacion de la funcion que pasamos como arguemnto
def minusculas(texto):
    return texto.lower()
saludar(minusculas)

#el clasico orden de higher orden functions es la funcion map
#esta funcion toma una funcion como referencia, y un iterable,llama  a la funcion base como referencia
#en cada elemento del iterable proporcionado
print(list(map(mayusculas,['texto1','texto2','texto3'])))
print(list(map(minusculas,['tExto1','TexTo2','tEXto3'])))

################
#funciones anidadas
def mostrar(texto):
    #definicion de la funcion interna o anidada
    def convertir_minusculas(t):
        return t.lower()
    #una vez definida la funcion interna la mandamos a llamar
    return convertir_minusculas(texto)

#cada vez que se llama la funcion mostrar se crea la funcion interna converitr minusculas
print(mostrar('Desde funcion anidada....'))
#no podemos utilizar la funcion interna desde fuera de la externa
#convertir_minusculas('texto1')
#mostrar.convertir_minusculas('HOLA')

#Retornar funcion anidada
#Observar que en ningun momento se retorna la funcion anidada desde la funcion externa
def hablar(volumen):
    def minusculas(texto):
        return texto.lower()
    def mayusculas(texto):
        return texto.upper()
    if volumen > .5:
        return mayusculas
    elif volumen <=.5:
        return minusculas
#utilizamos la funcion anidada

print(hablar(.8)('holi'))

variable_minusculas = hablar(0.4)
print(variable_minusculas('HABLO SUAVE'))

#################################
#Closure
#las funciones internas pueden capturar y guardar el estado de la funcion externa
def hablar_parametros(texto,volumen):
    #la funcion interna ya no recibe parametros
    def minusculas():
        return texto.lower()
    def mayusculas():
        return texto.upper()
    if volumen > .5:
        return mayusculas()
    elif volumen <=.5:
        return minusculas()
print(hablar_parametros('hablo fuerte',0.8))

#otro ejemplo de closure
#podemos preconfigurar una funcion
def mostrar(titulo):
    #definimos la funcion anidada o interna
    def saludar(mensaje):
        return titulo + '.'+mensaje
    return saludar

#preconfigurar 2 funciones

mostrar_ing = mostrar('Ingeniero')
mostrar_lic=mostrar('Licenciado')

#podemos seguir unsando el estado de la funcion previamente configurada aun que el valor de titulo ya esta fuera
#del alcance
print(mostrar_ing('Alvaro ruiz'))
print(mostrar_lic('Daniel tevez'))

#########################
# la funcion callable es para ver si un objeto se puede llamar o no ya q todas las funciones son objetos  pero no todos
#los objetos son funciones

print(f'Se puede llamar el objeto mostrar como funcion:{callable(mostrar)}')
print(f'Se puede llamar el objeto hablar como funcion:{callable(mostrar_lic)}')
print(f'Se puede llamar el objeto str como funcion? {callable("Hola")}')

#si queremos que una clase defina objetos que se puedan que se puedan llamar como funciones
#tenemos que sobreescribir el metodo __call__
class Mostrar:
    def __init__(self,titulo):
        self.titulo = titulo
    def __call__(self, mensaje):
        return self.titulo + '.'+mensaje
mostrar_doc=Mostrar('Doctor')
print(mostrar_doc('carlos ugalde'))
print(f'Se puede llamar el objeto mostrar doctor como una funcion:{callable(mostrar_doc)}')