import mysql.connector

personas_db = mysql.connector.connect(host='localhost', user='root', password='admin', database='personas_db')

cursor = personas_db.cursor()
sentencia_sql='DELETE FROM personas WHERE id_persona=%s'
valor=(6,)
cursor.execute(sentencia_sql,valor)
personas_db.commit()
print('Registro eliminado')
personas_db.close()