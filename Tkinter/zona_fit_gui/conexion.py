import mysql
from mysql.connector import pooling
from mysql.connector import Error
class Conexion:
    _DATABASE = 'zona_fit_db'
    _HOST = '127.0.0.1'
    _USER = 'root'
    _PASSWORD = 'admin'
    _PORT = 3306
    _POOL_SIZE = 5
    _POOL_NAME = 'zona_fit_pool'
    pool=None

    @classmethod
    def obtener_pool(cls):
        if cls.pool is None: #se crea un nuevo poool
            try:
                cls.pool = pooling.MySQLConnectionPool(pool_name=cls._POOL_NAME,
                                                       pool_size=cls._POOL_SIZE,
                                                       host=cls._HOST,
                                                       port=cls._PORT,
                                                       database=cls._DATABASE,
                                                       user=cls._USER,
                                                       password=cls._PASSWORD)
                #print(f'Nombre del pool: {cls.pool.pool_name}')
                #print(f'Tamaño del pool: {cls.pool.pool_size}')
                return cls.pool
            #esta clase error viene de mysql
            except Error as e:
                print(f'Ocurrio un error al obtener el pool: {e}')
        else:
            return cls.pool
    @classmethod
    def obtener_conexion(cls):
        return cls.obtener_pool().get_connection()
    @classmethod
    def liberar_conexion(cls,conexion):
        conexion.close()
        #print('Conexion cerrada')
if __name__ == '__main__':
    #creacion del objeto pool
    # pool = Conexion.obtener_pool()
    # print(pool)
    #obtener un objeto de conexion del pool
    conexion1=Conexion.obtener_conexion()
    print(conexion1)
    #cerrar objeto de conexion y regrese al pool
    Conexion.liberar_conexion(conexion1)
