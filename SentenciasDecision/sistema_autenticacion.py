print('****Sistema de autenticacion ***')
USUARIO_VALIDO= 'admin'
PASSWORD_VALIDO= '123'

usario = input('Ingresa el usuario: ').strip().lower()
password = input('Ingresa el password: ').strip().lower()

if usario == USUARIO_VALIDO and password == PASSWORD_VALIDO:
    print('Bienvenido al Sistema')
elif usario == USUARIO_VALIDO:
    print('Contraseña Incorrecta')
elif usario == PASSWORD_VALIDO:
    print('Usuario Incorrecto,Favor de corregirlo')
else:
    print('Usuario y password incorrectos')

