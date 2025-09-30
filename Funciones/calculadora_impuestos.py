print('Claculadora impuestos')

def calcular_tota_pago(pago_sin_impuesto:float,impuesto:float):
    pago_total=pago_sin_impuesto + pago_sin_impuesto*(impuesto/100)
    return pago_total

#ejecutamos la funcion
pago_sin_impuesto=float(input('Dame el valor del pago: '))
impuesto=float(input('Dame el valor del impuesto (en porciento): '))
pago_con_impuesto=calcular_tota_pago(pago_sin_impuesto,impuesto)
print(f'Pago con impuesto = {pago_con_impuesto}')