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
        self.labelConfiguracion.mousePressEvent = self.abrir_ventana_menu_configuracion
    
    def abrir_ventana_menu_principal(self, event):
        from menuPrincipal import VentanaMenuPrincipal
        
        self.ventana_menu = VentanaMenuPrincipal(self)  # Pasamos self como parent
        self.ventana_menu.show()
        self.hide()  # Ocultamos la ventana principal

    def abrir_ventana_menu_configuracion(self, event):
        from menuConfiguracion import VentanaMenuConfiguracion
        
        self.ventana_menu = VentanaMenuConfiguracion(self)
        self.ventana_menu.show()
        self.hide()
    
    def recabarDatos(self):#Obtener valores de los elementos
        nombrePerfil = self.lineEditNombrePerfil.text().strip()
        puestoDeseado = self.lineEditPuestoTrabajo.text().strip()
        areaFuncional = self.comboBoxAreaTrabajo.currentText().strip()
        escolaridad = self.comboBoxEscolaridad.currentText().strip()
        sueldoMinimo = self.lineEditSalarioMinimo.text().strip()
        sueldoMaximo = self.lineEditSalarioMaximo.text().strip()
        sector = self.lineEditSector.text().strip()
        ubicación = self.comboBoxUbicacion.currentText().strip()
        carrera = self.lineEditCarrera.text().strip()
        edad = self.lineEdad.text().strip()
        informacionAdicional = self.textEditInformacionAdicional.toPlainText().strip()
        herramientasDominadas = self.lineEditHerramientas.text().strip()
        habilidadesTecnicas = self.lineEditHabilidadesTecnicas.text().strip()
        habilidadesBlandas = self.lineEditHabilidadesBlandas.text().strip()
        logrosDestacados = self.lineEditLogros.text().strip()
        certificaciones = self.lineEditCertificaciones.text().strip()
        disponibilidad = self.comboBoxDisponibilidad.currentText().strip()
        idioma = self.comboBoxIdioma.currentText().strip()
        nivelIdioma = self.comboBoxNivelIdioma.currentText().strip()
        anosExperiencia = self.comboBoxAnosExperiencia.currentText().strip()
        titulacionRequerida = self.comboBoxTitulacion.currentText().strip()
        return (nombrePerfil, puestoDeseado, areaFuncional, escolaridad, sueldoMinimo, sueldoMaximo, sector, ubicación, carrera, edad, informacionAdicional, herramientasDominadas, habilidadesTecnicas, habilidadesBlandas, logrosDestacados, certificaciones, disponibilidad, idioma, nivelIdioma, anosExperiencia, titulacionRequerida)

    def insertar(self, *args):
        parametros = self.recabarDatos()
        if parametros:
            insertarPerfil(parametros)
            QMessageBox.information(self, "Éxito", "Perfil guardado exitosamente")
        elif parametros is None:
            QMessageBox.warning(self, "Error", "Por favor, complete todos los campos antes de guardar el perfil.")
    
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ventana = VentanaMenuAgregarPerfil()
    sys.exit(app.exec())