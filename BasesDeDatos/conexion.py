import psycopg2
import sys
from  logger_base import log
class Conexion:
    _DATABASE = 'test_dbs'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _conexion=None
    _cursor=None

    @classmethod
    def obtener_conexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = psycopg2.connect(host=cls._HOST,user=cls._USERNAME,password=cls._PASSWORD,port=cls._DB_PORT,dbname=cls._DATABASE)
                log.debug(f'Conexion exitosa : {cls._conexion}')
                return cls._conexion
            except Exception as e:
                log.debug(f'Ocurrio una exepcion {e}')
                sys.exit()
        else:
            return cls._conexion
    @classmethod
