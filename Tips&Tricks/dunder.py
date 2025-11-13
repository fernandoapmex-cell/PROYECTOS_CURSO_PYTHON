# si es un metodo under no se puede usar name amngling
#dunder significa doble under score
class Padre:
    def __init__(self):
        #aca si se puede usar NM
        self.__varible_dunder__=10
if __name__ == '__main__':
    padre=Padre()
    print('Accediendo a la variable dunder',padre.__varible_dunder__)