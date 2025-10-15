#Uunpacking - desempaquetado
valores = 1,2,3
print(valores)
print(type(valores))

valor1,valor2,valor3= 1,2,3
print(valor1,valor2,valor3)

valor1,_,valor3=1,2,3
print(valor1,valor3)
# el asteristco antes de la variable hace que todos los valores se le asignen a la variable 3 que se vuelve una lista
valor1,valor2,*valor3,valor4,valor5=[1,2,3,4,5,6,7,8,9]
print(valor1,valor2,valor3,valor4,valor5)


#unapcking en funciones

def regresa_varios_datos():
    return 1,2,3

valor1,valor2,valor3 = regresa_varios_datos()
print(valor1,valor2,valor3)

valor1,*valores_restantes=regresa_varios_datos()
print(valor1,valores_restantes)

#str.partition

hora,separador,minutos = '17:20'.partition(':')
print(hora,separador,minutos)