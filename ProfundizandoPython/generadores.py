#Generadores python
#es una funcion especial en python retorna una secuencia de valores
#suspende la ejecucion de la funcion yield (producir)(no se usa return)
def generador():
    yield 1
    print('Se reanuda la ejecucion')
    yield 2
    print('Se reanuda la ejecucion')
    yield 3

#consumimos el generador a demanda

gen =generador()
#con cada llamda consumimos un valor
print(next(gen))
print(next(gen))
print(next(gen))
#print(next(gen))
#si tratamos de llamar mas valores de los que produce el genrador manda un error de iterationStop

#consumiendo los valores del genrador con un for
gen = generador()
for valor in gen:
    print(valor)