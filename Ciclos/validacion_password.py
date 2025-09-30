print(' Creacion y validacion de contraseña ')

password = input('Ingresa un password (debe tener almenos 6 caracteres: ))')

while len(password) < 6:
    print('El passwords debe tener almenos 6 caracteres.')
    password = input('Ingresa un password (debe tener almenos 6 caracteres: ))')
else:
    print('El valor de password es correcto')
    