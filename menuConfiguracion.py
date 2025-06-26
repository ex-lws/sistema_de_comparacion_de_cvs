# Menu para poder acceder a las opciones de configuracion de la aplicacion.
# Permite borrar los curriculums y los datos de la base de datos.
import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox
from src_old.GestorBD import *
from src_old.AccionesCurriculum import *

class VentanaMenuConfiguracion(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)  # Pasamos el parent al constructor
        uic.loadUi('src_ui/menuConfiguracion.ui', self)
        self.configurar_label_clickeable()
        self.show()
        
    def configurar_label_clickeable(self):
        self.labelVolverInicio.setCursor(Qt.CursorShape.PointingHandCursor)
        self.labelVolverInicio.mousePressEvent = self.abrir_ventana_menu_principal
        self.labelBorrarCurriculums.mousePressEvent = self.borrar_curriculums
        self.labelBorrarDatos.mousePressEvent = self.borrar_datos
        self.labelBorrarResultados.mousePressEvent = self.borrar_resultados
    
    def abrir_ventana_menu_principal(self, event):
        from menuPrincipal import VentanaMenuPrincipal
        
        self.ventana_menu = VentanaMenuPrincipal(self)  # Pasamos self como parent
        self.ventana_menu.show()
        self.hide()  # Ocultamos la ventana principal

    def borrar_curriculums(self, *args):
        rutaCarpetaCurriculumsTemporales = "cvsTemporales"  # Cambia por tu ruta real
        rutaCarpetaCurriculumsDefinitivos = "cvsDefinitivos"  # Cambia por tu ruta real
        borrar_todos_los_archivos(rutaCarpetaCurriculumsTemporales)
        borrar_todos_los_archivos(rutaCarpetaCurriculumsDefinitivos)
        # Mostrar mensaje de éxito
        QMessageBox.information(self, "Éxito", "Currículums borrados exitosamente")
    
    def borrar_datos(self, *args):
        borrarBD()
        QMessageBox.information(self, "Éxito", "Datos borrados exitosamente")

    def borrar_resultados(self, *args):
        borrarTablaResultados()
        QMessageBox.information(self, "Éxito", "Resultados borrados exitosamente")
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ventana = VentanaMenuConfiguracion()
    sys.exit(app.exec())