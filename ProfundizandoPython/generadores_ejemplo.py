#generador de numeros del 1 al 5
def generador_numeros():
    for numero in range (1,6):
        yield numero
        print('Termina ejecucion')

#utilizamos el generador
generador = generador_numeros()
print(f'Objeto generador:{generador}')
print(type(generador))

#consumir el generador
for valor in generador:
    print(f'Numero producido por el generador {valor}')

#consumir a demanda
generador = generador_numeros()
try:
    print(f'consumir a demanda el generador:',next(generador))
    print(f'consumir a demanda el generador:',next(generador))
    print(f'consumir a demanda el generador:',next(generador))
    print(f'consumir a demanda el generador:',next(generador))
    print(f'consumir a demanda el generador:',next(generador))
    print(f'consumir a demanda el generador:',next(generador))
    print(f'consumir a demanda el generador:',next(generador))
    print(f'consumir a demanda el generador:',next(generador))
    print(f'consumir a demanda el generador:',next(generador))
    print(f'consumir a demanda el generador:',next(generador))
except Exception as e:
    print('fallo al consumir generador:',e)

#otra forma de consumir un generador
generador = generador_numeros()
while True:
    try:
        valor = next(generador)
        print(f'Numero producido por el generador {valor}')
    except Exception as e:
        print('fallo al consumir generador:',e)
        break
else:
    print('Termina ejeccion')
