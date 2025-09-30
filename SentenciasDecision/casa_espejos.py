print('***Bienvenidos a la casa de los espejos***')

edad=int(input('Ingrese su edad: '))
tienes_miedo_oscuridad=input('Ingrese si tienes miedo oscuridad:(Si/No)').strip().lower() == 'si'

if not tienes_miedo_oscuridad and edad >= 10:
    print('Puedes entrar a la casa de los espejos')
else:
    print('No puedes entrar a la casa de los espejos')
