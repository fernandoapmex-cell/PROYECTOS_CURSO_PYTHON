from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Eventos')
        self.etiqueta=QLabel('Da click en esta ventana')
        self.setCentralWidget(self.etiqueta)
    def mouseMoveEvent(self, evento):
        self.etiqueta.setText('Evento mouseMoveEvent detectado')
    def mousePressEvent(self, evento):
        if evento.button() == Qt.LeftButton:
            self.etiqueta.setText('Evento mousePressEvent boton izquierdo detectado')
        elif evento.button() == Qt.RightButton:
            self.etiqueta.setText('Evento mousePressEvent boton derecha detectado')
        elif evento.button() == Qt.MiddleButton:
            self.etiqueta.setText(f'Evento mousePressEvent boton medio detectado')
    def mouseReleaseEvent(self, evento):
        if evento.button() == Qt.LeftButton:
            self.etiqueta.setText('Evento mouseReleaseEvent boton izquierdo detectado')
        elif evento.button() == Qt.RightButton:
            self.etiqueta.setText('Evento mouseReleaseEvent boton derecha detectado')
        elif evento.button() == Qt.MiddleButton:
            self.etiqueta.setText(f'Evento mouseReleaseEvent boton medio detectado')
    def mouseDoubleClickEvent(self, evento):
        if evento.button() == Qt.LeftButton:
            self.etiqueta.setText('Evento mouseDoubleCLick boton izquierdo detectado')
        elif evento.button() == Qt.RightButton:
            self.etiqueta.setText('Evento mouseDoubleCLick boton derecha detectado')
        elif evento.button() == Qt.MiddleButton:
            self.etiqueta.setText(f'Evento mouseDoubleCLick boton medio detectado')


# ejecutamos prueba
if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()