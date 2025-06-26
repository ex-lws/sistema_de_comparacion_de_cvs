# Ventana para ver resultados
# Una clase se usa para quitar el BLOP de la tabla y mostrar un icono de PDF en su lugar.
# La otra clase pertenece a la ventana de ver resultados, que muestra los resultados.

import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox
from src_old.GestorBD import *
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QHeaderView
from PyQt6.QtWidgets import QStyledItemDelegate, QStyle, QApplication
from PyQt6.QtGui import QIcon, QPixmap

class PdfIconDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Usa un ícono de PDF local o uno estándar
        self.pdf_icon = QIcon("src_ui/iconoPdf.png")  # Cambia la ruta a tu ícono

    def paint(self, painter, option, index):
        # Solo mostrar el ícono en la columna del PDF
        if index.column() == 5:  # Cambia el índice según tu columna BLOB
            self.pdf_icon.paint(painter, option.rect, Qt.AlignmentFlag.AlignCenter)
        else:
            super().paint(painter, option, index)

    def displayText(self, value, locale):
        # No mostrar texto en la celda del PDF
        return ""


class VentanaMenuVerResultados(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)  # Pasamos el parent al constructor.
        uic.loadUi('src_ui/menuVerResultados.ui', self)
        self.conectar_bd()
        self.configurar_tabla()
        self.configurar_label_clickeable()
        self.personalizar_tableview()
        self.show()

    # Funciones para configurar todos los labels y widgets como clickeables y vincularlos a sus funciones.  
    def configurar_label_clickeable(self):
        self.labelVolverInicio.setCursor(Qt.CursorShape.PointingHandCursor)
        self.labelVolverInicio.mousePressEvent = self.abrir_ventana_menu_principal
        self.tableViewVerResultados.setModel(self.model)
        self.tableViewVerResultados.doubleClicked.connect(self.descargar_pdf)
        self.tableViewVerResultados.setItemDelegateForColumn(5, PdfIconDelegate(self))  # Cambia el 4 por el índice correcto
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
        self.model.setTable('resultados')
        self.model.select()
        self.model.setEditStrategy(QSqlTableModel.EditStrategy.OnManualSubmit)  # No permite edición directa
        # Renombrar los headers o encabezados.
        self.model.setHeaderData(0, Qt.Orientation.Horizontal, "ID")
        self.model.setHeaderData(1, Qt.Orientation.Horizontal, "Nombre del candidato")
        self.model.setHeaderData(2, Qt.Orientation.Horizontal, "Similitud")
        self.model.setHeaderData(3, Qt.Orientation.Horizontal, "Puesto deseado")
        self.model.setHeaderData(4, Qt.Orientation.Horizontal, "Resumen")
        self.model.setHeaderData(5, Qt.Orientation.Horizontal, "Curriculum")
        self.model.setHeaderData(6, Qt.Orientation.Horizontal, "Nombre del perfil")
        self.model.setHeaderData(7, Qt.Orientation.Horizontal, "ID del perfil")

    def personalizar_tableview(self):
        # Ocultar la columna de enumeración (vertical header)
        self.tableViewVerResultados.verticalHeader().setVisible(False)
        
        # Poner en negrita los encabezados de columna
        font = QFont()
        font.setBold(True)
        self.tableViewVerResultados.horizontalHeader().setFont(font)

        # Hacer que los encabezados ocupen todo el ancho del tableView
        header = self.tableViewVerResultados.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    def descargar_pdf(self, index):
    # Supón que la columna del BLOB es la 4 (ajusta según tu tabla)
        columna_pdf = 5
        if index.column() == columna_pdf:
            row = index.row()
            record = self.model.record(row)
            pdf_data = record.value("pdf_curriculum")
            if pdf_data:
                # Selecciona dónde guardar el archivo
                ruta, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Guardar PDF", "curriculum.pdf", "PDF Files (*.pdf)")
                if ruta:
                    with open(ruta, "wb") as f:
                        f.write(pdf_data)
                    QtWidgets.QMessageBox.information(self, "Éxito", "PDF guardado correctamente.")
            else:
                QtWidgets.QMessageBox.warning(self, "Error", "No hay PDF en este registro.")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ventana = VentanaMenuVerResultados()
    sys.exit(app.exec())