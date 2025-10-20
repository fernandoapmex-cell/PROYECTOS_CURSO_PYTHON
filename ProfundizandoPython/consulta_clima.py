import json
import urllib

respuesta=urllib.request.urlopen('https://globalmentoring.com.mx/api/clima.json')
print(respuesta)
cuerpo_respuesta=respuesta.read()
print(cuerpo_respuesta)
#procesamos la respuesta json
json_respuesta=json.loads(cuerpo_respuesta.decode('utf-8'))
print(json_respuesta)
#ejecicio 1.-Acceder a la descripcion del clima
descripcion_clima=json_respuesta.get('clima')[0].get('descripcion')
print(f'Descripcion del clima:{descripcion_clima}')
#otra forma de conseguir la descripcion del clima
descripcion_clima=json_respuesta['clima'][0]['descripcion']
print(f'Descripcion del clima:{descripcion_clima}')
#mostrar la temperatura minima y maxima
temp_min=json_respuesta.get('principal').get('temp_min')
print('Temperatura minima: ',temp_min)
temp_max=json_respuesta.get('principal').get('temp_max')
print('Temperatura maxima: ',temp_max)