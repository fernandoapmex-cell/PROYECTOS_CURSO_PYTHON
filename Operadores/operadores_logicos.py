#operador and
from operadores_asignacion import nombre

print('***operador logico and***')
#regrsa true si ambos parametros son verdaderos
condicion1= True
condicion2 = True
resultado = condicion1 and condicion2
print(f'Resultado de aplicar and en las condiciones :  {condicion1} y {condicion2} es : {resultado}')


print('***operador  logico or***')
#regrsa true si uno de ambos parametros es verdadero
condicion1= True
condicion2 = False
resultado = condicion1 or condicion2
print(f'Resultado de aplicar condicion or en las condiciones : {condicion1} y {condicion2} es : {resultado}')


print('***operador  logico not***')
condicion1= False
resultado= not condicion1
print(f'Resultado de aplicar condicion not en la condicion {condicion1} es :{resultado}')

#revisar si una variable es cadena vacia
nombre =' '
es_cadena_vacia = not nombre
print(f'Es cadena vacia : {es_cadena_vacia }')

#resivsar si una variable no tiene ningun variable asignado

variable = None
es_variable_vacia =  not variable
print(f'la variable no tiene ningun valor asignado?:{es_variable_vacia} ')