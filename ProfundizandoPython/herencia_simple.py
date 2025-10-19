#ejemplo herencia simple
class ListaSimple:
    def __init__(self,elementos):
        self._elementos=list(elementos)
    def agregar(self,elemento):
        self._elementos.append(elemento)
    def __getitem__(self,indice):
        return self._elementos[indice]
    def ordenar(self):
        self._elementos.sort()
    def __len__(self):
        return len(self._elementos)
    def __repr__(self):
    #representa el obj como string
        return f'{self.__class__.__name__}({self._elementos!r})'
class ListaOrdenado(ListaSimple):
    def __init__(self,elementos=[]):
        super().__init__(elementos)
        #ordenamos siempre los elementos una vez inicializados con el metodo de la clase padre
        self.ordenar()
    def agregar(self,elemento):
        super().agregar(elemento)
        #y luego ordenamos
        self.ordenar()
class ListaEnteros(ListaSimple):
    #esta list solo acepta numeros
    def __init__(self,elementos=[]):
        for elemento in elementos:
            self._validar(elemento)
            #si no arroja error el elementos y son validos con el metodo validar se agregan al atributo definido
            super().__init__(elementos)

    def _validar(self,elemento):
        #validamos si el elemento es de tipo entero
        if not isinstance(elemento,int):
            raise ValueError(f'El elemento {elemento} no es un entero')

    def agregar(self,elemento):
        self._validar(elemento)
        #una vez que ha sido validado lo agregamos a la lista
        super().agregar(elemento)



# lista_simple=ListaSimple([5,4,6,8])
# print(lista_simple)
lista_ordenada=ListaOrdenado([4,3,6,9,10,-1])
# print(lista_ordenada)
# lista_ordenada.agregar(-14)
# print(lista_ordenada)

#lista de enteros
lista_enteros=ListaEnteros([2,3,4,2,3])
# print(lista_enteros)

#is instance funciona para ver que tipo de objeto es conforme al MRO
print('Es entero',isinstance('10',int))
print('Es cadena',isinstance('str',str))
print('Es lista de enteros ordenada',isinstance(lista_enteros,ListaEnteros))

#es de varios tipos
print('Es de varios tipos',isinstance(lista_ordenada,(ListaSimple,ListaOrdenado,ListaEnteros)))