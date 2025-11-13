#Tip Las aserciones nos pueden ayudar a depurar nuestros programas de errores que no nos podemos recuperar

# Ejemplo 1. Revisamos si la division es entre 0

def dividir(a,b):
    #Nos aseguramos que el valor de b no es 0 para poder continuar con el programa
    assert b!= 0 ,'Divison entre cero'
    print(f'Resultado division:{a/b}')
# Ejemplo 2 Calculo del promedio de una lista de calificaciones
def obtener_promedio(calificaciones):
    #si la lista de calificaciones esta vacia no tiene que continuar el programa
    assert len(calificaciones) !=0 ,'Lista de calificaciones vacia'
    print((f'Promedio de calificaciones: {sum(calificaciones)/len(calificaciones)}'))
#ejemplo 3 realizamos un descuento a un producto
def aplicar_descuentos(productos,descuento):
    precio_con_descuento=productos['precio']*(1.0-descuento)
    print(f'Precio con descuento: {precio_con_descuento}')
    assert 0 <= precio_con_descuento <= productos['precio'],f'Descuento Invalido : {precio_con_descuento}'
    print('Descuento valido...')
if __name__ == '__main__':
    #dividir(10,3)
    #prueba del ejemplo 2
    obtener_promedio([10,8,9,7])
    #prueba del ejemplo 3 Aplicar descuento a un producto
    productos = {'nombre':'Camisa','precio':1500}
    aplicar_descuentos(productos,0.10)
