print('***Suma acumulativa***')
#sumar los primeros 5 numeros utilizando el ciclo while

MAXIMO = 50
numero = 1
Acumulador_suma=0

while numero <= MAXIMO:
    Acumulador_suma = Acumulador_suma + numero
    numero=numero + 1

print('Suma acumulada :',Acumulador_suma)
