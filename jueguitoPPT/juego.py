# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtGui import  QImageReader, QPixmap, QIcon
from PySide2 import QtCore
from ppt import Ui_Form

class QtWindow(QWidget):
    def __init__(self):
        super(QtWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setIcon()
        
        #Conexiones
        self.ui.opciones_CB.activated.connect(self.mostrarImagenUsuario)
        self.ui.jugar_PB.clicked.connect(self.mostrarImagenPc)
        self.ui.jugar_PB.setDisabled(True)
        self.ui.cerrar_PB.clicked.connect(self.closeMainWindow)

    def setIcon(self):
        appIcon = QIcon('mainIcon.png')
        self.setWindowIcon(appIcon)

    def closeMainWindow(self):
        
        QtCore.QCoreApplication.instance().quit()

    def mostrarImagenUsuario(self):

        self.ui.opcU2_LB.setVisible(False)

        sel = self.ui.opciones_CB.currentText()

        if sel == 'Piedra':
            reader = QImageReader('piedra.png')

        elif sel == 'Papel':
            reader = QImageReader('papel.png')

        elif sel == 'Tijeras':
            reader = QImageReader('tijeras.png')
        elif sel == 'Seleccionar':
            reader = QImageReader('esperar.png')
        else:
            self.ui.opcU1_LB.setVisible(False) 
            return

        reader.setAutoTransform(True)
        imagen = reader.read()

        self.ui.opcU1_LB.setPixmap(QPixmap.fromImage(imagen))
        self.ui.opcU1_LB.setVisible(True)

        self.ui.jugar_PB.setEnabled(True)  # Activar boton
        self.ui.msjGame_LB.clear()

    def mostrarImagenPc(self):

        self.ui.msjGame_LB.setText("En proceso")

        self.ui.jugar_PB.setDisabled(True)

if __name__ == "__main__":
    app = QApplication([])
    window = QtWindow()
    window.show()
    sys.exit(app.exec_())
