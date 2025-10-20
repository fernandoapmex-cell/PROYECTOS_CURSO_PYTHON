#leer el archivo de tipo Json JAVASCRIPT OBJECT NOTATION
import json
import urllib.request

respuesta=urllib.request.urlopen('https://globalmentoring.com.mx/api/personas.json')
print(respuesta)
#procesar el cuerpo de la respuesta
cuerpo_respuesta=respuesta.read()
print(cuerpo_respuesta)
#procesamos la respuesta que llegfa en binario
json_respuesta=json.loads(cuerpo_respuesta.decode('utf-8'))
print(json_respuesta)
#imprimir solo los nombres de las personas
#JSON se convierte en listas y diccionarios en python
for persona in json_respuesta['personas']:
    print(f'Persona:{persona["nombre"]} Edad:{persona["edad"]}')
#accedemos a las variables independientes
print(f'Total de personas: {json_respuesta["total"]}')
print(f'Mensaje:{json_respuesta["mensaje"]}')