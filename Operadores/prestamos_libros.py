print('***sistema de prestamo de libros***')

DISTANCIA_PERMITIDA_KM  = 3
tiene_credenciaL=input('¿Cuentas con credencial de estudiante?(Si/No) ').strip().lower()
distancia_biblioteca_km=int(input('Acuantos Kilometros vives de la biblioteca? '))

es_elebible_prestamo=tiene_credenciaL=='si' or distancia_biblioteca_km <= DISTANCIA_PERMITIDA_KM

print(f'eres elegible para un prestamo de libros: {es_elebible_prestamo}')


