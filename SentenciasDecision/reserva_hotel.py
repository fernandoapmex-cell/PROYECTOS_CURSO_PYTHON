print('***Sistema de reserva de hotel***')
#variables
TARIFA_DIARIA_SIN_VISTA_MAR=150.50
TARIFA_DIARIA_CON_VISTA_MAR=190.50
#PEDIMOS INFORMACION AL USUSARIO
nombre_cliente=input('Nombre Cliente: ')
dias_estadia=int(input('Dia de estadia: '))
vista_mar=input('Vista Mar(Si/No): ').strip().lower() =='si'

#calculamos costo total de la estancia

if vista_mar:
    costo_total=TARIFA_DIARIA_CON_VISTA_MAR * dias_estadia
else:
    costo_total=TARIFA_DIARIA_SIN_VISTA_MAR* dias_estadia

print(f'''

----------------DETALLES DE LA RESERVACION----------------

Nombre del cliente: {nombre_cliente}
Dias de estadia: {dias_estadia}
Costo total de la reservacion: ${costo_total:.2f}
Habitacion con vista al mar:{'Si'if vista_mar else 'No'}    
''')