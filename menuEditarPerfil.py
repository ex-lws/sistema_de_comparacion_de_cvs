# Ventana para eliminar perfiles

import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox
from src_old.GestorBD import *
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QHeaderView
from src_old.GestorBD import *
from PyQt6 import uic
from PyQt6.QtWidgets import QDialog

class VentanaMenuActualizarPefiles(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)  # Pasamos el parent al constructor.
        uic.loadUi('src_ui/menuEditarPerfil.ui', self)
        self.conectar_bd()
        self.configurar_tabla()
        self.configurar_label_clickeable()
        self.personalizar_tableview()
        self.show()

    # Funciones para configurar todos los labels y widgets como clickeables y vincularlos a sus funciones.  
    def configurar_label_clickeable(self):
        self.labelVolverInicio.setCursor(Qt.CursorShape.PointingHandCursor)
        self.labelVolverInicio.mousePressEvent = self.abrir_ventana_menu_principal
        self.tableViewVerPerfiles.setModel(self.model)
        self.labelConfiguracion.mousePressEvent = self.abrir_ventana_menu_configuracion
        self.labelRealizarEdicion.mousePressEvent = self.actualizar_perfil
    
    def abrir_ventana_menu_principal(self, event):
        # Importamos la ventana del menú principal y la mostramos para esta función.
        from menuEditarPerfilCampos import VentanaMenuEditarPerfilCampos
        self.ventana_ver = VentanaMenuEditarPerfilCampos(self)
        self.ventana_ver.show()
        #self.hide()  # Ocultamos la ventana principal

    def abrir_ventana_menu_configuracion(self, event):
        from menuConfiguracion import VentanaMenuConfiguracion
        
        self.ventana_menu = VentanaMenuConfiguracion(self)
        self.ventana_menu.show()
        self.hide()

    def conectar_bd(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('BD/Perfiles.bd')
        if not db.open():
            print("No se pudo conectar a la base de datos")

    def configurar_tabla(self):
        self.model = QSqlTableModel(self)
        self.model.setTable('perfiles')
        self.model.select()
        # Renombrar los headers o encabezados.
        self.model.setHeaderData(0, Qt.Orientation.Horizontal, "ID")
        self.model.setHeaderData(1, Qt.Orientation.Horizontal, "Nombre del perfil")
        self.model.setHeaderData(2, Qt.Orientation.Horizontal, "Contratación")
        self.model.setHeaderData(3, Qt.Orientation.Horizontal, "Horario de trabajo")
        self.model.setHeaderData(4, Qt.Orientation.Horizontal, "Modalidad")
        self.model.setHeaderData(5, Qt.Orientation.Horizontal, "Sueldo MAX")
        self.model.setHeaderData(6, Qt.Orientation.Horizontal, "Sueldo MIN")
        self.model.setHeaderData(7, Qt.Orientation.Horizontal, "Escolaridad")
        self.model.setHeaderData(8, Qt.Orientation.Horizontal, "Área")
        self.model.setHeaderData(9, Qt.Orientation.Horizontal, "Puesto")
        self.model.setHeaderData(10, Qt.Orientation.Horizontal, "Ubicación")
        self.model.setHeaderData(11, Qt.Orientation.Horizontal, "Idioma")
        self.model.setHeaderData(12, Qt.Orientation.Horizontal, "Nivel de idioma")
        self.model.setHeaderData(13, Qt.Orientation.Horizontal, "Licencia de conducir")
        self.model.setHeaderData(14, Qt.Orientation.Horizontal, "Años de experiencia")

    def personalizar_tableview(self):
        # Ocultar la columna de enumeración (vertical header)
        self.tableViewVerPerfiles.verticalHeader().setVisible(False)
        
        # Poner en negrita los encabezados de columna
        font = QFont()
        font.setBold(True)
        self.tableViewVerPerfiles.horizontalHeader().setFont(font)

        # Hacer que los encabezados ocupen todo el ancho del tableView35
        header = self.tableViewVerPerfiles.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    def actualizar_perfil(self, *args):
        print("Actualizando perfil...")
        


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ventana = VentanaMenuActualizarPefiles()
    sys.exit(app.exec())