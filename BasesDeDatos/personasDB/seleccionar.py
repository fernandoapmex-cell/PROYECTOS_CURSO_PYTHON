import mysql.connector

personas_db = mysql.connector.connect(host='localhost', user='root', password='admin', database='personas_db')

mi_cursor=personas_db.cursor()
mi_cursor.execute("SELECT nombre_persona,edad_persona,apellido_persona FROM personas")
resultado=mi_cursor.fetchall()
for persona in resultado:
    print(persona)
#cerrar conexion
personas_db.close()