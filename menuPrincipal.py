# menuPrincipal.py (modificado)
import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt


class VentanaMenuPrincipal(QtWidgets.QMainWindow):
    def __init__(self, parent):
        self.parent = parent
        super().__init__()
        uic.loadUi('src_ui/menuPrincipal.ui', self)
        self.configurar_label_clickeable()
        self.show()
    
    def configurar_label_clickeable(self):
        self.labelAnadiPerfiles.setCursor(Qt.CursorShape.PointingHandCursor)
        self.labelAnadiPerfiles.mousePressEvent = self.abrir_ventana_agregar_perfil
    
    def abrir_ventana_agregar_perfil(self, event):
        from menuAgregarPerfil import VentanaMenuAgregarPerfil
        
        self.ventana_agregar = VentanaMenuAgregarPerfil(self)  # Pasamos self como parent
        self.ventana_agregar.show()
        self.hide()  # Ocultamos la ventana principal

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ventanaMenuPrincipal = VentanaMenuPrincipal(None)  # Pasamos None como parent inicial
    sys.exit(app.exec())