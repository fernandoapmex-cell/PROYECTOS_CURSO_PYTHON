print('Convertir temperaturas ')

def celcius_fahrenheint(celcius):
    return celcius * 9 / 5 + 32

#funcion que convierte de fahrenheint a celcius

def fahrenheit_celcius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

#programa principal

celcius = float(input('Dame el valor de celcius: '))
resultado= celcius_fahrenheint(celcius)
print(f'El resultado de la temperatura en celsius {celcius:.2f} a fahrenheint es: {resultado:.2f}')

fahrenheit = float(input('Dame el valor de fahrenheit: '))
resultado= fahrenheit_celcius(fahrenheit)
print(f'El resultado de la temperatura en fahrenheit {celcius:.2f} a celsius es: {resultado:.2f}')

