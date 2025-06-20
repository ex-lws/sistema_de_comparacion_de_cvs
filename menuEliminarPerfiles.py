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

class VentanaMenuEliminarPefiles(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)  # Pasamos el parent al constructor.
        uic.loadUi('src_ui/menuEliminarPerfil.ui', self)
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
        self.labelRealizarEliminacion.mousePressEvent = self.eliminar_perfil
    
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

    def eliminar_perfil(self, *args):
        
        # Variables requeridas para eliminar un perfil.
        # booleana para verificar si el ID existe.
        # Eliminar un perfil requiere de un ID de perfil.

        id_perfil_eliminar = (self.lineEditIdPerfilEliminar.text().strip())
        id_existe = existe_id_perfil(id_perfil_eliminar)

        if id_existe:
            id_perfil_eliminar = int(id_perfil_eliminar)  # Convertimos a entero para la función de eliminación.
            eliminarPerfil(id_perfil_eliminar)
            QMessageBox.information(self, "Éxito", "Perfil eliminado de manera exitosa.")
            self.model.select() # Actualizamos el modelo para reflejar los cambios en la tabla.
            self.lineEditIdPerfilEliminar.clear()
            

        elif not id_perfil_eliminar:
            QMessageBox.warning(self, "Advertencia", "Por favor, ingrese un ID de perfil para eliminar.")
            return
        elif id_perfil_eliminar.isdigit() == False:
            QMessageBox.warning(self, "Advertencia", "El ID del perfil debe ser un número entero.")
            return
        
        elif not id_existe:
            QMessageBox.warning(self, "Advertencia", f"No existe un perfil con el ID {id_perfil_eliminar}.")
            return
        


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ventana = VentanaMenuEliminarPefiles()
    sys.exit(app.exec())