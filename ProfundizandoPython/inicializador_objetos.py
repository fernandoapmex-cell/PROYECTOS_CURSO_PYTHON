class Padre:
    def __init__(self):
        print('Inicializador Padre')
    def metodo(self):
        print('Metodo de Padre')



class Hijo(Padre):
    #si defino el init aca ya no se llama el de la clase padre
    def __init__(self):
        #de manera opcional podemos llamar al metodo init de la clase padre o super
        super().__init__()
        print('Inicializador Hijo')
    def metodo(self):
        print('Metodo de padre sobreescrito hijo')
        #asi se llama al metodo de la clase padre del mismo metodo
        super().metodo()

# padre1=Padre()
# #llamamos el metodo con el objeto
# padre1.metodo()
#
# hijo=Hijo()
# hijo.metodo()
hijo1=Hijo()
hijo1.metodo()