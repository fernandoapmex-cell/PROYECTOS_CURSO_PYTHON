print('***Sistema de calificaiones ***')
calficaion = float(input('proporciona una calificacion entre 0 y 10: '))
#revisamos si esta en los siguientes rangos
calificacion_letra= None
if 9 <= calficaion <= 10:
    calficaion_letra = 'A'
elif 8 <= calficaion < 9:
    calficaion_letra = 'B'
elif 7 <= calficaion < 8:
    calficaion_letra = 'C'
elif 6 <= calficaion < 7:
    calficaion_letra = 'D'
elif 0 <= calficaion < 6:
    calficaion_letra = 'F'
else:
    calficaion_letra = 'Calificacion Incorrecta'

print(f'Calificacion {calficaion} es equivalente a {calficaion_letra}')