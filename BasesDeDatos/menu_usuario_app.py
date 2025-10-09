from usuario import Usuario
from usuario_dao import usuarioDAO
from logger_base import log
opcion = None
while opcion != 5:
    print('''
    Opciones:
    1.-Lista de usuarios
    2.-Agregar ususario
    3.-Modificar usuario
    4.-Eliminar usuario
    5.-Salir    
    \n''')
    opcion = int(input('Ingrese una opcion: \n'))
    if opcion == 1:
        usuarios=usuarioDAO.seleccionar()
        #iteramos los objetos usuario
        for usuario in usuarios:
            log.info(usuario)
    elif opcion == 2:
        #se usa var para variables temporales
        nombre_usuario_var=input('Ingrese su nombre de usuario: ')
        password_usuario_var=input('Ingrese su password de usuario: ')
        usuario = Usuario(nombre_usuario=nombre_usuario_var,password_usuario=password_usuario_var)
        usuarios_insertados = usuarioDAO.insertar(usuario)
        log.info(f'Usuarios insertados : {usuarios_insertados}')
    elif opcion == 3:
        id_usuario_var=input('Ingrese su id de usuario: ')
        nombre_usuario_var=input(f'Ingrese el nuevo nombre de usuario del id_usuario {id_usuario_var}: ')
        password_usuario_var=input(f'Ingrese el nuevo password de usuario del id_usuario {id_usuario_var}: ')
        usuario = Usuario(id_usuario_var,nombre_usuario_var,password_usuario_var)
        usuarios_actualizados = usuarioDAO.actualizar(usuario)
        log.info(f'Usuarios actualizados : {usuarios_actualizados}')
    elif opcion == 4:
        id_usuario_var=int(input('Ingrese su id de usuario a eliminar: '))
        usuario=Usuario(id_usuario=id_usuario_var)
        usuarios_eliminados = usuarioDAO.eliminar(usuario)
        log.info(f'Usuarios eliminados : {usuarios_eliminados}')
else:
    log.info('Salimos de la aplicacion...')