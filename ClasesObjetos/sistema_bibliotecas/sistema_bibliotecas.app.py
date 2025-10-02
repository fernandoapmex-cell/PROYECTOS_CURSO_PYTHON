from ClasesObjetos.sistema_bibliotecas.biblioteca import Biblioteca
from ClasesObjetos.sistema_bibliotecas.libro import Libro
bibliotecaNacional =Biblioteca('Biblioteca Nacional')
print(f'*** Bienvenidos a la biblioteca : {bibliotecaNacional.get_nombre} ***')

#Definicion de libros

libro1 = Libro('Cien años de soledad','Gabriel Garcia Marquez','Ficcion')
libro2 = Libro('Don Quijote d ela mancha','Miguel de Cervantes','COmedia')
libro3= Libro('El amor en los tiempos de colera','Gabriel Garcia Marquez','Ficcion')
libro4= Libro('Pedro Paramo','Juan rulfo','Ficcion')
libro5= Libro('Pantaleon y los visitadores','Mario Vargas Iosa','Comedia')

#agregar libros a la biblioteca nacional

bibliotecaNacional.agregar_libro(libro1)
bibliotecaNacional.agregar_libro(libro2)
bibliotecaNacional.agregar_libro(libro3)
bibliotecaNacional.agregar_libro(libro4)
bibliotecaNacional.agregar_libro(libro5)

#Buscar Libros por autor

autor = "Gabriel Garcia Marquez"
print(f'\n Libros de {autor}')
bibliotecaNacional.buscar_libros_autor(autor)

#Buscar Libros por genero

genero = "Ficcion"
print(f'\n Libros por genero: {genero}')
bibliotecaNacional.buscar_libros_genero(genero)

#Mostrar todos los libros
bibliotecaNacional.mostrar_todos_libros()