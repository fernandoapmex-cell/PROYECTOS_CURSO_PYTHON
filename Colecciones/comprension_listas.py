print('*** Comprension de listas ***')

#Una lista con el cuadrado de cada numero

numeros=[1,2,3,4,5]
cuadrados=[x**2 for x in numeros]
print(cuadrados)

#lista de cuadrados de pares

numeros=range(10+1)
pares=[x**2 for x in numeros if x %2 ==0]
print(pares)

#lista saludando a cada nombre

nombres= ['Ana','Jeronimo','Carlos']
saludando=[f'Hola {nombre}' for nombre in nombres]
print(saludando)
