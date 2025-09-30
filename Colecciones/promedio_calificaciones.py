print('****Promedio de calificaciones***')
total_calificaciones=int(input('proporciona la cantidad de calificaciones ha evaluar: '))
calificaciones=[]
#iterar las calificaciones
for indice in range(total_calificaciones):
    calificacion = float(input(f'Ingresa la calificacion numero {indice+1}: '))
    calificaciones.append(calificacion)
#imprimimos las calificaciones proporcionadas
    print(f'\n Las calificaciones proporcionadas son {calificaciones}')
#calculamos el promedio
#con funcion sum sumas todo lo de un objeto de lista
suma_calificaciones = sum(calificaciones)
promedio_calificaciones=suma_calificaciones/total_calificaciones
print(f'\nEl promedio de las calificaciones proporcionadas es : {promedio_calificaciones:.1f}')