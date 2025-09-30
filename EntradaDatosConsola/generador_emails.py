print('***Sistema generador de emails***')
nombre= input('Introduce tu nombre: ')
apellidos= input('Introduce tu apellido: ')
empresa= input('Introduce tu empresa: ')
extension_dominio= input('Introduce tu extension dominio de tu empresa: ')

#normalizamos los valores recibidos
nombre=nombre.strip().lower().replace(' ','.')
apellidos=apellidos.strip().lower().replace(' ','.')
empresa=empresa.strip().lower().replace(' ','')
extension_dominio=extension_dominio.strip().lower().replace(' ','.')

#generar email

email=f'{nombre}.{apellidos}@{empresa}{extension_dominio}'
print(f'''
Tu nuevo email genrado por el sistema es:
    {email}
    Felicidades!''')
