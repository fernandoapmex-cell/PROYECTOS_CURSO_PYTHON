print('***Combinacion de listas y tuplas ***')
#definir la lista que almacenara las tuplas
productos=[
    ('P001','Camiseta',20.00),
    ('P002','Jens',30.00),
    ('P003','Sudadera',40.00)
]

#imprimir la informacion de cada producto
# y ademas calculamos el precio total
precio_total=0

print('Informacion de los productos : ')
for producto in productos:
    #usamos unpacking
    id,descripcion,precio = producto
    print(f'id = {id}, descripcion = {descripcion}, precio = {precio}')
    precio_total = precio_total + precio

print(f'Precio total de los productos: ${precio_total}')