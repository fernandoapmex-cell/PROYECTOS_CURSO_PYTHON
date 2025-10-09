from psycopg2 import pool
import sys
from  logger_base import log


class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CONNECTIONS = 1
    _MAX_CONNECTIONS = 5
    _pool=None

    @classmethod
    def obtener_pool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(
                cls._MIN_CONNECTIONS,
                cls._MAX_CONNECTIONS,
                host=cls._HOST,
                user=cls._USERNAME,
                password=cls._PASSWORD,
                port=cls._DB_PORT,
                database=cls._DATABASE)
                log.debug(f'Creacion del pool exitosa:{cls._pool}')
            except Exception as e:
                log.error(f'Ocurrio un error al obtener el pool {e}')
                sys.exit()
        return cls._pool
    @classmethod
    def obtener_conexion(cls):
        conexion = cls.obtener_pool().getconn()
        log.debug(f'Conexion obtenida del pool: {conexion}')
        return conexion
    @classmethod
    def liberar_conexion(cls,conexion):
        cls.obtener_pool().putconn(conexion)
        log.debug(f'Se regreso la conexion al pool :{conexion}')
    @classmethod
    def cerrar_conexiones(cls):
        cls.obtener_pool().closeall()
        log.debug('Pool de conexiones cerrado')
if __name__ == '__main__':
    conexion1=Conexion.obtener_conexion()
    conexion1=Conexion.liberar_conexion(conexion1)
    conexion2=Conexion.obtener_conexion()
    # conexion3=Conexion.obtener_conexion()
    # conexion4=Conexion.obtener_conexion()
    # conexion5=Conexion.obtener_conexion()

