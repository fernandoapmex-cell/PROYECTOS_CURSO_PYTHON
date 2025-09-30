print('***Calculo Area y Perimetro de un rectangulo***')

base=float(input('Ingresa la base del rectangulo: '))
altura=float(input('Ingresa la altura del rectangulo: '))

# Realizamos los calculs

area= base*altura
perimetro = 2 * (base+altura)

print(f'El area del rectangulo es de: {area}, y su perimetro es de: {perimetro}')