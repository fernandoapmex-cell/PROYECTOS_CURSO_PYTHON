from conexion import Conexion
from logger_base import log
class CursorPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None
    def __enter__(self):
        log.debug('inicio del metodo with __enter__')
        self._conexion= Conexion.obtener_conexion()
        self._cursor=self._conexion.cursor()
        return self._cursor
    def __exit__(self, tipo_excepcion,valor_excepcion,detalle_excepcion):
        log.debug('Se ejecuta metodo __exit__')
        if tipo_excepcion != None:
            self._conexion.rollback()
            log.error(f'Ocurrio una excepcion :{valor_excepcion},{tipo_excepcion},{detalle_excepcion}')
        else:
            self._conexion.commit()
            log.debug(f'Commit de la transaccion realizada!')
        #cerrar el cursor
        self._cursor.close()
        Conexion.liberar_conexion(self._conexion)

if __name__ == '__main__':
    with CursorPool() as cursor:
        cursor.execute("SELECT * FROM persona ORDER BY id_persona ASC")
        log.debug(cursor.fetchall())