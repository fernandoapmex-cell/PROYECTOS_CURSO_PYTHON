print('***Bienvenido al sistema bancario***')
salir_sistema_txt=input('¿Deseas salir del sistema?(Si/No)')
salir_sistema_bool= salir_sistema_txt.strip().lower() =='si'

if not salir_sistema_bool:
    print('continuamos dentro del sistema')
else:
    print('Salimos del sistema')