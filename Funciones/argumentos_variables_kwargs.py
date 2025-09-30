def superheroe_superpoderes(nombre,*args,**kwargs):
    print(f'Superheroe:{nombre} - {args} - Mas Info: {kwargs}')

#llamamos la funcion
superheroe_superpoderes('spiderman','Instinto Aragnido',edad=17,empresa='Marvel')
superheroe_superpoderes('Ironman','Armadura',edad= 45)

#Es opcional enviar argumentos variables
