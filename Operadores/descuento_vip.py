print('***sistema de descuento VIP**')

NO_PRODUCTO_DESCUENTO=10
cantidadad_productos_diarios=int(input('Cuantos productos compraste hoy?' ))
tiene_membresia=input('tiene membresia de la tienda? (Si/No)').strip().lower()

es_elegible_descuento_vip=(cantidadad_productos_diarios >= NO_PRODUCTO_DESCUENTO
                           and tiene_membresia == 'si')

print(f'es elegible para el descuento VIP: {es_elegible_descuento_vip}')
