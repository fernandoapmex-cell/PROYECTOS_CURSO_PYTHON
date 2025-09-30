#conversion de tipos de datos
from enum import nonmember
from statistics import variance

#convertir cadena a numero

numero_cadena='10'
numero_entero=int(numero_cadena)
print(f'valor numerico de cadena en entero:{numero_entero}')

#convertir cadena a flotante

numero_cadena='3.14'
numero_flotante=float(numero_cadena)
print(f'valor numerico de cadena en flotante:{numero_flotante}')

#convertir numero a cadena

numero_entero = 25
numero_cadena=str(numero_entero)
print(f'valor numerico a cadena :{numero_cadena}')

# Tipo bool es Falso en los sgguientes casos
# Si eI valor es O, cadena vacia, o None, entonces False
# True, si el valor es distinto de 0, si es distinto de cadena vacia
# y tambien si es distinto de None

numero_entero= 2
booleano = bool(numero_entero)
print(f'valor boleano de numero entero es: {booleano}')

cadena=' '
booleano= bool(cadena)
print(f'valor boleano de cadena es: {booleano}')

variable= None
booleano = bool(variable)
print(f'valor de None es:{booleano}')