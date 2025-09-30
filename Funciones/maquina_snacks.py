print('****Sistema de maquina de snacks***')

#definimos la lista de snacks inicial

snacks=[
    {'id':1,'nombre':'Papas','precio':30},
    {'id': 2, 'nombre': 'Refresco', 'precio':50},
    {'id': 3, 'nombre': 'Sandwcich', 'precio':120}
]

#lista de productos (vacia) son los snacks ya comprados
productos_comprados= [

]

def mostrar_snacks():
    print('---- Snacks Disponibles ----')
    for snack in snacks:
       print(f'Id:{snack.get("id")} -> {snack.get("nombre")}'
             f' - ${snack.get("precio")}')


def buscar_snack_id(id_snack):
    for snack in snacks:
        if snack.get("id") == id_snack:
            return snack
    return None

def comprar_snacks():
    id_snack =int(input('Que snack quieres comprar (id): '))
    snack_encontrado= buscar_snack_id(id_snack)
    if snack_encontrado is not None:
        productos_comprados.append(snack_encontrado)
        print(f'Snack comprado : {snack_encontrado.get("nombre")}')
    else:
        print(f'Snack no encontrado con el id {id_snack}')

def mostar_ticket():
    ticket = f'\t--- Ticket de venta ---'
    total = 0
    for producto in productos_comprados:
        ticket +=f'\n\t - {producto.get("nombre")} --- ${producto.get("precio")} '
        total = total + producto.get("precio")
    ticket += f'\n\tTotal de venta: ${total}'
    print(ticket)
#programa principal

if __name__ == '__main__':
    # creamos menu de la aplicacion
    while True:
        print(f'''
        1.-Mostrar Snacks
        2.-Comprar Snacks
        3.-Mostar Ticket
        4.-Salir
        ''')
        opcion= int(input('Escoge la opcion deseada del 1- 4: '))
        if opcion == 1:
            mostrar_snacks()
        elif opcion == 2:
            comprar_snacks()
        elif opcion == 3:
            mostar_ticket()
        elif opcion == 4:
            print('Hasta Pronto!')
            break
        else:
            print('Opcion no valida,Ingrese una opcion valida')

