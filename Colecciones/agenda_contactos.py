print('****Agenda de diccionarios ***')

agenda = {
    "Carlos":{
        "Telefono": "22444564",
        "E-mail": "carlos@mail.com",
        "Direccion": "Calle Principal 132",
    },
    "Maria": {
        "Telefono": "99887733",
        "E-mail": "maria@mail.com",
        "Direccion": "Avenida Central 456",
    },
    "Pedro": {
        "Telefono": "55139078",
        "E-mail": "pedro@mail.com",
        "Direccion": "Plaza Mayor 789",
    }
}
print(agenda)

#accder a la informacion de un contacto en especifico

print(f'''
    Informacion del contacto de Maria:
    Telefono:{agenda['Maria']['Telefono']}
    Direccion:{agenda['Maria']['Direccion']}
    Email:{agenda.get('Maria').get('E-mail')}
''')

#agregar un nuevo contacto


agenda['Ana']={
    "Telefono": "445666444",
    "E-mail": "ana@mail.com",
    "Direccion": "Avenida Rosales 4567",
}

print(agenda)

agenda.pop('Pedro')


print(agenda)

#Contactos en la agenda
print('Contactos en la agenda')
for nombre,detalles in agenda.items():
    print(f'''
    Nombre:{nombre}
     Telefono:{detalles.get("Telefono")}
     Direccion:{detalles.get("Direccion")}
     Email:{detalles.get("E-mail")}    
    ''')
