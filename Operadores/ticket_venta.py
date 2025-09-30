print('***Genenracion de ticket de venta***')
precio_leche= float(input('Ingrese el precio de la leche: '))
precio_pan= float(input('Ingrese el precio de la pan: '))
precio_lechuga= float(input('Ingrese el precio de la lechuga: '))
precio_platanos=float(input('Ingrese el precio de la platanos: '))
descuento_porcentaje=int(input('Aplicar algun descuento en porcentaje(%):  '))

#calculo subtotal sin impuestos

subtotal = precio_leche+precio_pan+precio_lechuga+precio_platanos

#aplica a algun descuento

descuento = subtotal*(descuento_porcentaje/100)

#calculamos el subtotal con descuento

subtotal_con_descuento= subtotal-descuento

#calculo con impuestos (16%)

impuesto = subtotal_con_descuento * 0.16

#calculo total de compra con impuestos

costo_total_compra = subtotal_con_descuento + impuesto
print(f'''
Subtotal = ${subtotal:.2f}
Descuento = ${descuento:.2f}(%{descuento_porcentaje})
Subtotal con descuento = ${subtotal_con_descuento:.2f}
Impuesto (16%)= ${impuesto:.2f}
Total = ${costo_total_compra:.2f}
''')