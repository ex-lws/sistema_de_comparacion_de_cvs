# Ventana para ver perfiles

import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox
from src_old.GestorBD import *
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QHeaderView

class VentanaMenuVerPefiles(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)  # Pasamos el parent al constructor.
        uic.loadUi('src_ui/menuVerPerfiles.ui', self)
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
    
    def abrir_ventana_menu_principal(self, event):
        # Importamos la ventana del menú principal y la mostramos para esta función.
        from menuPrincipal import VentanaMenuPrincipal
        self.ventana_menu = VentanaMenuPrincipal(self)  # Pasamos self como parent
        self.ventana_menu.show()
        self.hide()  # Ocultamos la ventana principal

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
        self.model.setEditStrategy(QSqlTableModel.EditStrategy.OnManualSubmit)  # No permite edición directa

        # Renombrar los headers o encabezados según la definición de la tabla
        self.model.setHeaderData(0, Qt.Orientation.Horizontal, "ID")
        self.model.setHeaderData(1, Qt.Orientation.Horizontal, "Nombre del perfil")
        self.model.setHeaderData(2, Qt.Orientation.Horizontal, "Puesto deseado")
        self.model.setHeaderData(3, Qt.Orientation.Horizontal, "Área funcional")
        self.model.setHeaderData(4, Qt.Orientation.Horizontal, "Escolaridad")
        self.model.setHeaderData(5, Qt.Orientation.Horizontal, "Sueldo mensual mínimo")
        self.model.setHeaderData(6, Qt.Orientation.Horizontal, "Sueldo mensual máximo")
        self.model.setHeaderData(7, Qt.Orientation.Horizontal, "Sector")
        self.model.setHeaderData(8, Qt.Orientation.Horizontal, "Ubicación")
        self.model.setHeaderData(9, Qt.Orientation.Horizontal, "Carrera")
        self.model.setHeaderData(10, Qt.Orientation.Horizontal, "Edad")
        self.model.setHeaderData(11, Qt.Orientation.Horizontal, "Información adicional")
        self.model.setHeaderData(12, Qt.Orientation.Horizontal, "Herramientas dominadas")
        self.model.setHeaderData(13, Qt.Orientation.Horizontal, "Habilidades técnicas")
        self.model.setHeaderData(14, Qt.Orientation.Horizontal, "Habilidades blandas")
        self.model.setHeaderData(15, Qt.Orientation.Horizontal, "Logros destacados")
        self.model.setHeaderData(16, Qt.Orientation.Horizontal, "Certificaciones")
        self.model.setHeaderData(17, Qt.Orientation.Horizontal, "Disponibilidad")
        self.model.setHeaderData(18, Qt.Orientation.Horizontal, "Idioma")
        self.model.setHeaderData(19, Qt.Orientation.Horizontal, "Nivel de idioma")
        self.model.setHeaderData(20, Qt.Orientation.Horizontal, "Años de experiencia")
        self.model.setHeaderData(21, Qt.Orientation.Horizontal, "Titulación requerida")

    def personalizar_tableview(self):
        # Ocultar la columna de enumeración (vertical header)
        self.tableViewVerPerfiles.verticalHeader().setVisible(False)
        self.tableViewVerPerfiles.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        
        # Poner en negrita los encabezados de columna
        font = QFont()
        font.setBold(True)
        self.tableViewVerPerfiles.horizontalHeader().setFont(font)

        # Hacer que los encabezados ocupen todo el ancho del tableView
        header = self.tableViewVerPerfiles.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
    

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ventana = VentanaMenuVerPefiles()
    sys.exit(app.exec())