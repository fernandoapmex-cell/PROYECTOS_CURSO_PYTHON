#el guion bajo simple se utiliza por convencion y se usa para indicar que una variable es temporal o sin importancia
for _ in range(3):
    print('Hola...',_)

#tambien lo podemos usar cuando trabajamos con tuplas
valores = ('Juan','Perez',31)
nombre,_,edad = valores
print(f'Nombre: {nombre}')
print(f'Edad: {edad}')

#se puede usar una lista como variable temporal
_=list()
_.append(1)
_.append(2)
_.append(3)
print(_)
