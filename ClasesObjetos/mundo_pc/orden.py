class Orden:

    contador_ordenes = 0
    def __init__(self,computadoras:list):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes + 1
        #recibimos la lista de objetos de tipo computadoras
        self._computadoras = computadoras
    def agregar_computadora(self,computadora):
        self._computadoras.append(computadora)
    def __str__(self):
        computadoras_str = ''
        for computadora in self._computadoras:
            computadoras_str += '\n' + computadora.__str__()
        return f'''
        Orden : {self._id_orden}
        Computadoras:{computadoras_str}
        '''
