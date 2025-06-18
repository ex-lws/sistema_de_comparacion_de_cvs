# menuAgregarPerfil.py (modificado)
import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox
from src_old.GestorBD import *

class VentanaMenuAgregarPerfil(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)  # Pasamos el parent al constructor
        uic.loadUi('src_ui/menuAgregarPerfil.ui', self)
        self.configurar_label_clickeable()
        self.show()
        
    def configurar_label_clickeable(self):
        self.labelVolverInicio.setCursor(Qt.CursorShape.PointingHandCursor)
        self.labelVolverInicio.mousePressEvent = self.abrir_ventana_menu_principal
        self.labelAgregarPerfil.mousePressEvent = self.insertar
    
    def abrir_ventana_menu_principal(self, event):
        from menuPrincipal import VentanaMenuPrincipal
        
        self.ventana_menu = VentanaMenuPrincipal(self)  # Pasamos self como parent
        self.ventana_menu.show()
        self.hide()  # Ocultamos la ventana principal
    
    def recabarDatos(self):#Obtener valores de los elementos
        nombrePerfil = self.lineEditNombrePerfil.text().strip()
        Tipocontratación = self.comboBoxTipoContratacion.currentText().strip()
        Horariotrabajo = self.comboBoxHorarioTrabajo.currentText().strip()
        Modalidadtrabajo = self.comboBoxModalidadTrabajo.currentText().strip()
        Salariominimo = self.lineEditSalarioMinimo.text().strip()
        Salariomaximo = self.lineEditSalarioMaximo.text().strip()
        Escolaridad = self.comboBoxEscolaridad.currentText().strip()
        Areatrabajo = self.comboBoxAreaTrabajo.currentText().strip()
        Puesto = self.lineEditPuestoTrabajo.text().strip()
        Ubicación = self.comboBoxUbicacion.currentText().strip()
        Idioma = self.comboBoxIdioma.currentText().strip()
        Nivelidioma = self.comboBoxNivelIdioma.currentText().strip()
        Licenciaconducir = self.comboBoxLicenciaConducir.currentText().strip()
        Anosexperiencia = self.lineEditExperiencia.text().strip()

        return (nombrePerfil, Tipocontratación, Horariotrabajo, Modalidadtrabajo, Salariominimo, Salariomaximo, Escolaridad, Areatrabajo, Puesto, Ubicación, Idioma, Nivelidioma, Licenciaconducir, Anosexperiencia)

    def insertar(self, *args):
        parametros = self.recabarDatos()
        insertarPerfil(parametros)
        QMessageBox.information(self, "Éxito", "Perfil guardado exitosamente")
    
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ventana = VentanaMenuAgregarPerfil()
    sys.exit(app.exec())