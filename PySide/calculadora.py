from functools import partial
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QLineEdit, QGridLayout, QPushButton


class Calculadora(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculadora')
        self.setFixedSize(235,235)
        self.componente_general=QWidget(self)
        self.setCentralWidget(self.componente_general)
        #creamos un layout principal
        self.layout_principal=QVBoxLayout()
        self.componente_general.setLayout(self.layout_principal)
        #Metodo para crear la parte visual de la calculadora
        self._crear_area_captura()
        #agregamos los botones de la calculadora
        self._crear_botones()
        #conectamos las señales con los slots que vamos a asociar a cada uno de los botones
        self._conectar_botones()

    def _crear_area_captura(self):
        self.linea_entrada=QLineEdit()
        self.linea_entrada.setFixedHeight(35)
        self.linea_entrada.setAlignment(Qt.AlignRight)
        self.linea_entrada.setReadOnly(True)
        #agregamos la linea de entrada configurada al layout principal
        self.layout_principal.addWidget(self.linea_entrada)
    def _crear_botones(self):
        #creamos un diccionario para definir el texto de cada boton y posicion
        self.botones={}
        layout_botones=QGridLayout()
        #texto | posicion en el grid layout
        self.botones = {
            #se agrega el texcto y la posicion
            '7':(0,0),
            '8':(0,1),
            '9':(0,2),
            '/':(0,3),
            '4':(1,0),
            '5':(1,1),
            '6':(1,2),
            '*':(1,3),
            '1':(2,0),
            '2':(2,1),
            '3':(2,2),
            '-':(2,3),
            '0':(3,0),
            '.':(3,1),
            'C':(3,2),
            '+':(3,3),
            '=':(3,4),
        }
        #creamos los botones y los agregamos al grid layout
        #la posicion es una tupla de dos valores (renglon-columna)
        #con el for se recorre el diccionario y se saca llave y valor
        for texto_boton,posicion in self.botones.items():
            self.botones[texto_boton]=QPushButton(texto_boton)
            self.botones[texto_boton].setFixedSize(40,40)
            #publicamos el boton en el grid layout
            layout_botones.addWidget(self.botones[texto_boton],posicion[0],posicion[1])
        #agregamos el layout de botones al layout principal
        self.layout_principal.addLayout(layout_botones)
    def _conectar_botones(self):
        #recorrer cada boton con del diccionario (key:value)(texto:PushButton)
        for texto_boton,boton in self.botones.items():
            if texto_boton not in {'=','C'}:
                #lambada aca no sirve
                #boton.clicked.connect(lambda :self._construir_expresion(texto_boton))
                boton.clicked.connect(partial(self._construir_expresion,texto_boton))
            self.botones['C'].clicked.connect(self._limpiar_linea_entrada)
            #conectamos el boton de igual
            self.botones['='].clicked.connect(self._calcular_resultado)
            self.linea_entrada.returnPressed.connect(self._calcular_resultado)
    def _construir_expresion(self,texto_boton):
        expresion = self.obtener_texto() + texto_boton
        #Actualizamos la linea de entrada
        self.actualizar_texto(expresion)
    def obtener_texto(self):
        return self.linea_entrada.text()
    def actualizar_texto(self,texto_boton):
        self.linea_entrada.setText(texto_boton)
        self.linea_entrada.setFocus()
    def _limpiar_linea_entrada(self):
        self.actualizar_texto('')
    def _calcular_resultado(self):
        resultado=self._evaluar_experesion(self.obtener_texto())
        self.actualizar_texto(resultado)
    def _evaluar_experesion(self,expresion):
        try:
            #utilizamos eval para evaluar la expresion
            resultado=str(eval(expresion))
        except Exception as e:
            resultado='Syntax Error limpiar con C'
        return resultado





if __name__ == '__main__':
    app= QApplication()
    calculadora=Calculadora()
    calculadora.show()
    app.exec()