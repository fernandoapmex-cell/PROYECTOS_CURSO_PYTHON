from conexion import Conexion
from cliente import Cliente
class ClienteDAO:
    _SELECCIONAR='SELECT * FROM clientes'
    _INSERTAR='INSERT INTO clientes(nombre_cliente,apellido_cliente,membresia_cliente) VALUES (%s,%s,%s)'
    _ACTUALIZAR='UPDATE clientes SET nombre_cliente = %s, apellido_cliente = %s, membresia_cliente = %s WHERE id_cliente = %s'
    _ELIMINAR='DELETE FROM clientes WHERE id_cliente = %s'

    @classmethod
    def seleccionar(cls):
        #se usa afuera para que el metodo reconozca la variable
        conexion=None
        try:
            conexion=Conexion.obtener_conexion()
            cursor=conexion.cursor()
            cursor.execute(cls._SELECCIONAR)
            registros=cursor.fetchall()
            #mapeo de clase tabla
            clientes=[]
            for registro in registros:
                cliente = Cliente( registro[0], registro[1], registro[2], registro[3] )
                clientes.append(cliente)
            return clientes
        except Exception as e:
            print(f'Ocurrio un error al seleccionar clientes: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)
    @classmethod
    def insertar(cls,cliente):
        conexion=None
        try:
            conexion=Conexion.obtener_conexion()
            cursor=conexion.cursor()
            valores=(cliente._nombre_cliente,cliente.apellido_cliente,cliente.membresia_cliente)
            cursor.execute(cls._INSERTAR,valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al insertar cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)
    @classmethod
    def actualizar(cls,cliente):
        conexion=None
        try:
            conexion=Conexion.obtener_conexion()
            cursor=conexion.cursor()
            valores=(cliente._nombre_cliente,cliente.apellido_cliente,cliente.membresia_cliente,cliente.id_cliente)
            cursor.execute(cls._ACTUALIZAR,valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
           print(f'Ocurrio un error al actualizar cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)
    @classmethod
    def eliminar(cls,cliente):
        conexion=None
        try:
            conexion=Conexion.obtener_conexion()
            cursor=conexion.cursor()
            valores=(cliente.id_cliente,)
            cursor.execute(cls._ELIMINAR,valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
           print(f'Ocurrio un error al eliminar cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

if __name__ == '__main__':
    pass
    #insertar cliente

    # cliente1= Cliente(nombre_cliente='Chabelo',apellido_cliente='Canelas',membresia_cliente=890)
    # clientes_insertados=ClienteDAO.insertar(cliente1)
    # print(f'Se insertaron {clientes_insertados} clientes!')

    #acutualizar clientes
    # cliente1=Cliente(4,'Chaman','Gerber',69)
    # clientes_actualizados = ClienteDAO.actualizar(cliente1)


    #eliminar cliente

    # cliente1 = Cliente(id_cliente=4)
    # clientes_eliminados=ClienteDAO.eliminar(cliente1)
    # print(f'Se eliminaron {clientes_eliminados} clientes!')

    #seleccionar clientes
    # clientes=ClienteDAO.seleccionar()
    # for cliente in clientes:
    #     print(cliente)