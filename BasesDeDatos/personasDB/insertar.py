import mysql.connector

personas_db = mysql.connector.connect(host='localhost', user='root', password='admin', database='personas_db')

mi_cursor=personas_db.cursor()
sentencia_sql=('INSERT INTO personas(nombre_persona,apellido_persona,edad_persona) VALUES (%s,%s,%s)')
valores=('Victor','Ramos',46)
mi_cursor.execute(sentencia_sql,valores)
personas_db.commit()#este comando guarda los cambios en la base de datos
personas_db.close()