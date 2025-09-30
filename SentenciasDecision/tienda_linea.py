print('Sistema de tienda en linea con descuento')
#CONDICIONES
MONTO_COMPRAS_DESC= 1000

monto_compra=float(input('Ingresa el monto de tu compra : '))
es_miembro=input('Eres miembro de la tienda?(Si/No): ').strip().lower()

descuento = 0

if monto_compra >= MONTO_COMPRAS_DESC and es_miembro == 'si':
    descuento = 0.1 #Descuento del 10%
elif es_miembro == 'si':
    descuento = 0.05 #Descuento del 5%
elif monto_compra >= MONTO_COMPRAS_DESC :
    descuento = 0.03 #descuentro del 3%
else:
    descuento = 0

#hacemos calculos para obtener el descuento final

if descuento !=0:
    monto_descuento = monto_compra  * descuento
    monto_final=monto_compra - monto_descuento
    print(f'''
    Felicidades ,has obtenido un descuento de : {descuento*100:.0f} % 
    Monto de la compra:${monto_compra:.2f}
    Monto de descuento:${monto_descuento:.2f}
    Monto final de la conmpra con descuento:${monto_final:.2f}
    ''')
else:
    print('No haz obtenido descuento por tu compra!')
    print('Te invitamos a hacerte miembro de la tienda')
    print(f'Monto final de la compra: ${monto_compra:.2f}')





