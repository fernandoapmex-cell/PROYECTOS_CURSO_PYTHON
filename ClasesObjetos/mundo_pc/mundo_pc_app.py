from ClasesObjetos.mundo_pc.computadora import Computadora
from ClasesObjetos.mundo_pc.monitor import Monitor
from ClasesObjetos.mundo_pc.orden import Orden
from ClasesObjetos.mundo_pc.raton import Raton
from ClasesObjetos.mundo_pc.teclado import Teclado

print('**** Mundo PC ****')
teclado1 = Teclado('gamecraft', 'bluetooth')
raton1 = Raton('hp', 'usb')
monitor1 = Monitor('dell', 28.6)
computadora1 = Computadora('hp', monitor1, teclado1, raton1)

teclado2 = Teclado('razer', 'bluetooth')
raton2 = Raton('logi', 'cable')
monitor2 = Monitor('acer', 30.6)
computadora2 = Computadora('alienware', monitor2, teclado2, raton2)


teclado3 = Teclado('corsair', 'cable')
raton3 = Raton('logi', 'usb')
monitor3 = Monitor('gigabyte', 38.6)
computadora3 = Computadora('samsung', monitor3, teclado3, raton3)

teclado4 = Teclado('denuvo', 'bluetooth')
raton4 = Raton('gobierno', 'usb')
monitor4 = Monitor('lenovo', 70.6)
computadora4 = Computadora('lenovo', monitor4, teclado4, raton4)


teclado5 = Teclado('alaska', 'cable')
raton5 = Raton('coppel', 'usb')
monitor5 = Monitor('lg', 15.6)
computadora5 = Computadora('lg', monitor5, teclado5, raton5)

#crear la lista de computadoras para el constructor de orden
computadoras = [computadora1,computadora2]
orden1 = Orden(computadoras)
print(orden1)
computadoras=[computadora3,computadora4]
orden2 = Orden(computadoras)
print(orden2)
computadoras=[computadora5]
orden3 = Orden(computadoras)
print(orden3)

