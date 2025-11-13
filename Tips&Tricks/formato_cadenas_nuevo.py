#2.-Nuevo Estilo de formato de cadenas en py
nombre = 'Juan'
mi_cadena= 'Hola,{}'.format(nombre)
print(mi_cadena)
#podemos convertir enteros a hexa
error = 500
cadena_hexa='Error en hexadecimal :{e1:x}'.format(e1=error)
print(cadena_hexa)
#ejemplo entero a flotante
entero = 50
cadena_flotante='Error en flotante :{entero:.2f}'.format(entero=entero)
print(cadena_flotante)
#usando f string
#podemos hacer lo mismo pero de manera simplificado y sando stirng interpolation o f-string literal
mi_cadena = f'hola,{nombre}'
print(mi_cadena)
#este es el mismo ejemplo de hexa con string interpolation
print(f'Errror en hexadecimal :{error:x}')
#el mismo ejemplo de impresion de entero a flotante
print(f'Numero flotante:{entero:.2f}')
#podemos incluir expresiones o llamdas a funciones
a = 10
b = 3
print(f'Dividimos y damos formato:{a/b:.2f}')