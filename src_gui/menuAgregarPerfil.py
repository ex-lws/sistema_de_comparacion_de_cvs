# menuAgregarPerfil.py (modificado)
import sys
from PyQt6 import QtWidgets, uic

class VentanaMenuAgregarPerfil(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)  # Pasamos el parent al constructor
        uic.loadUi('src_ui/menuAgregarPerfil.ui', self)
        
        # Guardamos referencia al parent
        self.parent = parent
        
        # Configurar botón de regreso (si existe)
        if hasattr(self, 'btnRegresar'):
            self.btnRegresar.clicked.connect(self.regresar_menu_principal)
        
        self.show()
    
    def regresar_menu_principal(self):
        """Método para volver al menú principal"""
        if self.parent:
            self.parent.show()  # Mostramos la ventana principal
        self.close()  # Cerramos esta ventana
    
    def closeEvent(self, event):
        """Evento al cerrar la ventana"""
        if self.parent:
            self.parent.show()  # Mostramos la ventana principal al cerrar
        super().closeEvent(event)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ventana = VentanaMenuAgregarPerfil()
    sys.exit(app.exec())