print('***Argumentos Variables***')

def superheroe_superpoderes(superheore,nombre,*args):
    print(f'superheore: {superheore} - nombre: {nombre} - args: {args}')
    #iteramos los superpoderes
    for superpoder in args:
        print(f'superpoder: {superpoder}')

#llamar la funcion

superheroe_superpoderes('Spiderman','Peter Parker','Instinto Aragnido','Telaraña')
superheroe_superpoderes('ironman','tony stark','Instinto Aragnido','Telaraña',"playboy")

