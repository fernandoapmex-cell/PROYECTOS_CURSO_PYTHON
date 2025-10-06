from numeros_identicos_exception import NumerosIdenticosException
resultado = None

try:
    a = int(input("Introduce un numero 1 : "))
    b = int(input("Introduce un numero 2 : "))
    if a ==b:
        raise NumerosIdenticosException('Numeros identicos')
    resultado = a / b
except ZeroDivisionError as e:
    print(f'Exception - Ocurrio un error: {e}, Tipo de error : {type(e)}')
except TypeError as e:
    print(f'Exception - Ocurrio un error: {e}, Tipo de error :  {type(e)}')
#siempre pondremos la excepcin general al final
except Exception as e:
    print(f'Exception - Ocurrio un error: {e},  Tipo de error : {type(e)}')
else:
    print(f'No se arrojo ninguna excepcion')
finally:
    print('Finalizando...')
print(f'Resultado:', resultado)
print('Continuamos...')