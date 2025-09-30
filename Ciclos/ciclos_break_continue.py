print('Break and continue')

#ejemplo con break
print('Usando break')
for numero in range(1,10,1):
    if numero % 2 == 0:
        print(numero,end=' ')
        break
print('\n\n')
print('Usando continue \n')
for numero in range(1,10,1):
    if numero % 2 == 1:
        print(numero) # numeros impares
        continue
    #print(numero) # numeros pares