#sirve para desempaquetar
numeros=[1,2,3]
print(numeros)
#aca desepaqueta la lista separando los valores y ya no es una lista
#se pueden pasar separadores
print(*numeros,sep='-')

#unpacking en argumentos
#desempaquetando al momento de pasar parametros a una funcion
def sumar(a,b,c):
    print(f'Resultado suma : {a+b+c}')

sumar(*numeros)

# Extraer algunas partes de una lista
mi_lista=[1,2,3,4,5,6]
a,*b,c,d=mi_lista
print(a,b,c,d)

# unir lista

lista1=[1,2,3]
lista2=[4,5,6]
lista3=[lista1,lista2]
print(lista3)
lista3=[*lista1,*lista2]
#aca ya no se genera una matriz ya se unen las dos listas en una
print(lista3)

#para diccionarios se utiliza el doble asterisco

#unir diccionarios

dic={'A':1,'B':2,'C': 3}
dic2={'D':4,'E':5,'F':6}
dic3={**dic,**dic2}
print(dic3)

#construir una lista apartir de un string
lista=[*'Holamundo']
#si usamos dos veces el * se separa la lista y crea una cadena y separa cada digito
print(*lista,sep='-')
