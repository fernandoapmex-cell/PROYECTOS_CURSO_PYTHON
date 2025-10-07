import psycopg2

conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432',database='test_db')
#print(conexion)
try:
    with conexion:
        #creamos un cursor sirve para ejetuar sentencias sql en postgres
        with conexion.cursor() as cursor:

            #seleccionar registros

            # sentencia='SELECT * FROM persona WHERE id_persona IN %s'
            # entrada=input('Proporciona los id\'s a buscar (separado por comas): ')
            # llaves_primarias =  ( tuple(entrada.split(',')),)
            # #aca usare el %s que es un placeholder pa pasar un valor en forma de tupla
            # #id_persona = input('Introduce el ID persona: ')
            # cursor.execute(sentencia,llaves_primarias)
            # #cambie a fetchone para que regrese solo 1 valor osea quita la lista de tuplas y solo regresa una tupla
            # registros = cursor.fetchall()
            # for registro in registros:
            #     print(registro)

            #insertar un registro

            # sentencia = 'INSERT INTO persona(nombre,apellido,email) VALUES (%s,%s,%s)'
            # valores = ('carlos','lara','clara@mail.com')
            # cursor.execute(sentencia,valores)
            # #commit guarda los cambios en la base de datos pero como estamos usando with lo hace automaticamente
            # #conexion.commit()
            # #aca nos dice cuantos registros se metieron en el cursor actual
            # registros_insertados=cursor.rowcount
            # print('registros insertados: ',registros_insertados)

            #insertar varios registros

            # sentencia = 'INSERT INTO persona(nombre,apellido,email) VALUES (%s,%s,%s)'
            # valores = (('chibelo','juarez','chive@mail.com'),('marcos','cantu','mcantu@mail.com'),('Maria','gonzalez','mgonzalez@mail.com'))
            # cursor.executemany(sentencia,valores)
            # #commit guarda los cambios en la base de datos pero como estamos usando with lo hace automaticamente
            # #conexion.commit()
            # #aca nos dice cuantos registros se metieron en el cursor actual
            # #aca nos dice cuantos registros se metieron en el cursor actual
            # registros_insertados=cursor.rowcount
            # print('registros insertados: ',registros_insertados)

            #actualizar registros

            # sentencia = 'UPDATE persona SET nombre=%s,apellido=%s,email=%s WHERE id_persona=%s'
            # valores = ('Juan carlos','Juarez' ,'jcjuarez@mail.com',1)
            # cursor.execute(sentencia,valores)
            # registros_actualizados=cursor.rowcount
            # print('registros actualizados: ',registros_actualizados)

            #actualizar varios registros

            # sentencia = 'UPDATE persona SET nombre=%s,apellido=%s,email=%s WHERE id_persona=%s'
            # valores = (
            #     ('Juan','Perez','jperez@mail.com',1),
            #     ('Chamalla','gutierrez','cgutierrez@mail.com',2)
            # )
            # cursor.executemany(sentencia,valores)
            # registros_actualizados=cursor.rowcount
            # print('registros actualizados: ',registros_actualizados)

            #eliminar registros
            # sentencia = 'DELETE FROM persona WHERE id_persona=%s'
            # entrada = input('proporciona el id del registro a eliminar')
            # valores = (entrada,)
            # cursor.execute(sentencia, valores)
            # registros_eliminados=cursor.rowcount
            # print('registros eliminados: ',registros_eliminados)

            #eliminar varios registros a la vez
            sentencia = 'DELETE FROM persona WHERE id_persona IN %s'
            entrada = input('proporciona los id de registros a eliminar separados por una coma: ')
            valores=(tuple(entrada.split(',')),)
            cursor.execute(sentencia,valores)
            registros_eliminados = cursor.rowcount
            print('registros eliminados:',registros_eliminados)


except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
3