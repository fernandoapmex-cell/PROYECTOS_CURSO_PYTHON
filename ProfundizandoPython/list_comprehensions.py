numeros =range(10)
lista_pares=[]

#creamos una nueva lista con los valores pares multiplicados por si mismo
for numero in numeros:
    #revisamos si es un numero par
    if numero % 2 == 0:
        lista_pares.append(numero*numero)
print('Lista de pares :',lista_pares)
#hacemos lo mismo pero con list comprenhensions
#[Expresion for var in coleccionif condicion]
#la condicion de if es opcional
lista_pares=[]
lista_pares=[numero*numero for numero in numeros if numero % 2 == 0]
print('Lista de pares con List comprenhensions:',lista_pares)

#un ejemplo similar pero con 2 condiciones
#solo se agrega el valor a la lista cuando el valor cumple ambas condiciones
#es decir,debe de ser un numero dibisible entre 2 y entre 6.
pares=[numero for numero in range(50) if numero%2==0 and numero% 6 ==0]
print('Lista de pares con List comprenhensions:',pares)

#ejemplo agregando if else

lista_pares=[]
lista_impares=[]
for numero in range(10):
    if numero % 2 == 0:
        lista_pares.append(numero)
    elif numero % 2 == 1:
        lista_impares.append(numero)
print(f'Pares: {lista_pares}')
print(f'Impares: {lista_impares}')

#mismo ejercicio con list comprehensions
lista_pares=[]
lista_impares=[]
[lista_pares.append(numero) if numero%2==0 else lista_impares.append(numero) for numero in range(50)]
print('Lista de pares con List comprenhensions:',lista_pares)
print(f'Lista de impares con List comprenhensions:: {lista_impares}')

#lista de listas

lista_listas=[[1,2,3],[4,5,6],[7,8,9,10]]
#crear una lista simple de la matriz

lista_simple=[valor for sublista in lista_listas for valor in sublista]
print('Lista simple con List comprenhensions:',lista_simple)
#lista de pares a partir de la lista de listas
#sin list comprehensions,ciclos for anidados
lista_pares=[]
lista_impares=[]
for sublista in lista_listas:
    for valor in sublista:
        if valor % 2 == 0:
            lista_pares.append(valor)
        elif valor % 2 == 1:
            lista_impares.append(valor)
print(f'Lista de pares sin List comprenhensions:: {lista_pares}')
print(f'Lista de impares sin List comprenhensions:: {lista_impares}')
lista_pares=[valor for sublista in lista_listas for valor in sublista if valor % 2 == 0]
lista_impares=[valor for sublista in lista_listas for valor in sublista if valor % 2 == 1]
print('Lista de pares con List comprenhensions:',lista_pares)
print('Lista de impares con List comprenhensions:',lista_impares)
#con list comprenhensions en una sola linea de codigo
