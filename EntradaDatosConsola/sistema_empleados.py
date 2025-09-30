print('***sistema de empleados***')
nombre_empleado=input('Introduce el nombre del empleado: ')
edad_empleado=int(input('Introduce la edad del empleado: '))
salario_empleado=float(input('Introduce el salario del empleado: '))
es_jefe_departamento=input('Introduce si es jefe de departamento:(Si/No) ')

#vamos a convertir un tipo bool la variable es jefe de departamento
es_jefe_departamento=es_jefe_departamento.lower() == 'si'

#Imprimir los valores del empleado

print('\n Datos del Enpleado')
print(f'Nombre del empleado: {nombre_empleado}')
print(f'Edad del empleado: {edad_empleado}')
print(f'Salario del empleado: {salario_empleado:.2f}')# el :.2f es para especificar cuantos decimales se van a ver
print(f'Es Jefe de departamento: {es_jefe_departamento}')

