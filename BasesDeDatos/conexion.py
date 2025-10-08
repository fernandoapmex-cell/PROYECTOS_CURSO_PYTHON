import psycopg2
import sys
from  logger_base import log
class Conexion:
    _DATABASE = 'test_db'
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
                log.error(f'Ocurrio una exepcion al obtener la conexion:{e}')
                sys.exit()
        else:
            return cls._conexion
    @classmethod
    def obtener_cursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtener_conexion().cursor()
                log.debug(f'Se abrio el cursor correctamente : {cls._cursor}')
                return cls._cursor
            except Exception as e:
                log.error(f'Ocurrio una exepcion al obtener el cursor:{e}')
                sys.exit()
        else:
            return cls._cursor

if __name__ == '__main__':
        #Conexion.obtener_conexion()
        Conexion.obtener_cursor()
