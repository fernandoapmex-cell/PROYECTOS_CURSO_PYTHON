from servicio.catalogo_peliculas import CatalogoPeliculas
from dominio.pelicula import Pelicula


opcion = None
while opcion != 4:
    try:
        print('Opciones : ')
        print('1.-Agregar pelicula')
        print('2.- Lista de peliculas')
        print('3.- Eliminar catalogo peliculas')
        print('4.- Salir')
        opcion = int(input('Escribe tu opcion(1-4): '))
        if opcion == 1:
            nombre = input('Ingrese el nombre de la pelicula ')
            pelicula = Pelicula(nombre)
            CatalogoPeliculas.agregar_pelicula(pelicula)
        elif opcion == 2:
            CatalogoPeliculas.listar_peliculas()
        elif opcion == 3:
            CatalogoPeliculas.eliminar_peliculas()
    except Exception as e:
        print(f'Ocurrio un error: {e}')
        opcion = None
else:
    print('Salimos del programa')