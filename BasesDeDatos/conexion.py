from contextlib import closing

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
    _pool_=None

    @classmethod
    def obtener_pool(cls):
        if cls._pool_ is None:
            try:
            except Exception as e:
                log.error(f'Ocurrio un error al obtener el pool {e}')
    @classmethod
    def obtener_conexion(cls):
        pass



