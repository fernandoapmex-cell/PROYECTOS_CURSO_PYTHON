print('Funcion Par')

#funcion para saber si un par es par o no

def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


#llamamos a nuestra funcion

if __name__ == '__main__':
    numero = int(input('Ingresa un numero: '))
    print(f'Es par : {es_par(numero)}')