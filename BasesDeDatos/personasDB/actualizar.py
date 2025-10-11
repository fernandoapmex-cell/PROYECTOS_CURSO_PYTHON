import mysql.connector

personas_db = mysql.connector.connect(host='localhost', user='root', password='admin', database='personas_db')

mi_cursor=personas_db.cursor()
sentencia_sql=('UPDATE personas SET nombre_persona=%s,apellido_persona=%s,edad_persona=%s WHERE id_persona=%s')
valores=('Victorina','Ramos',46,5)
mi_cursor.execute(sentencia_sql,valores)
personas_db.commit()#este comando guarda los cambios en la base de datos
personas_db.close()
print('Se ha modificado la tabla')