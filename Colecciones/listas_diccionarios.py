print(' Listas y diccionarios')

personas=[
    {
        'nombre':'Regina',
        'apellido':'Flores',
        'edad':21,
    }
    ,
    {
        'nombre': 'Alejandro',
        'apellido': 'Reyes',
        'edad': 32,
    }
]
print(personas)

#acceder a un diccionario desde una lista
print(f'''
    Nombre:{personas[0].get("Nombre")}
    Apellido:{personas[0].get("Apellido")}
    Edad:{personas[0].get("Edad")}
''')

#recorrer los elementos de la lista

for contador ,persona in enumerate(personas):
    print(f'{contador} - Persona : {persona}')
    print(f'Detalle:\n Nombre:{persona.get('nombre')},Apellido:{persona.get('apellido')}')