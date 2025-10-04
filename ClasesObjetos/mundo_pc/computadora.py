from ClasesObjetos.mundo_pc.monitor import Monitor
from ClasesObjetos.mundo_pc.teclado import Teclado
from ClasesObjetos.mundo_pc.raton import Raton

class Computadora:
    contador_computadoras= 0

    def __init__(self,nombre,monitor:Monitor,teclado:Teclado,raton:Raton):
        Computadora.contador_computadoras+=1
        self._id_computadora= Computadora.contador_computadoras
        self._nombre= nombre
        self._monitor= monitor
        self._teclado= teclado
        self._raton= raton

    def __str__(self):
        return f'''
            {self._nombre.upper()} : {self._id_computadora}
            Monitor : {self._monitor}
            Teclado : {self._teclado}
            Raton : {self._raton}
        '''

#prueba

if __name__ == '__main__':
    teclado1=Teclado('gamecraft','bluetooth')
    raton1=Raton('hp','usb')
    monitor1=Monitor('dell',28.6)
    computadora1 = Computadora('hp',monitor1,teclado1,raton1)
    print(computadora1)

    teclado2=Teclado('razer','bluetooth')
    raton2=Raton('logi','cable')
    monitor2=Monitor('acer',30.6)
    computadora2= Computadora('alienware',monitor2,teclado2,raton2)
    print(computadora2)