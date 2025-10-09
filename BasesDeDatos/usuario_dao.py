from cursor_pool import CursorPool
from logger_base import log
from usuario import Usuario


class usuarioDAO:
    '''
    DAO- Data Access Object para la tabla de usuario
    '''
    _SELECT = 'SELECT * FROM usuario'
    _INSERT = 'INSERT INTO usuario (nombre_usuario,password_usuario) VALUES (%s, %s)'
    _ACTUALIZAR='UPDATE usuario SET nombre_usuario=%s ,password_usuario = %s WHERE id_usuario = %s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario = %s'

    @classmethod
    def seleccionar(cls):
        with CursorPool() as cursor:
            log.debug('Seleccionando usuarios...')
            cursor.execute(cls._SELECT)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0],registro[1],registro[2])
                usuarios.append(usuario)
            return usuarios

    @classmethod
    def insertar(cls,usuario):
        with CursorPool() as cursor:
            log.debug(f'Insertando usuario {usuario}...')
            valores=(usuario.nombre_usuario,usuario.password_usuario)
            cursor.execute(cls._INSERT,valores)
            return cursor.rowcount

    @classmethod
    def actualizar(cls,usuario):
        with CursorPool() as cursor:
            log.debug(f'Actualizando usuario {usuario}...')
            valores=(usuario.nombre_usuario,usuario.password_usuario,usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR,valores)
            return cursor.rowcount

    @classmethod
    def eliminar(cls,usuario):
        with CursorPool() as cursor:
            log.debug(f'Eliminando usuario {usuario}...')
            valores = (usuario.id_usuario,)
            cursor.execute(cls._ELIMINAR,valores)
            return cursor.rowcount