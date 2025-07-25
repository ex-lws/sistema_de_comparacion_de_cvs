# Ventana para poder realizar compraciones entre CV's y los perfiles de los candidatos.

import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox
from src_old.GestorBD import *
from src_old.RealizarComparacion import *
from src_old.AccionesCurriculum import *
from src_old.SeleccionarPerfilParaComparar import *
from src_old.GenerarResumen import *
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QHeaderView

class VentanaMenuComparacion(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)  # Pasamos el parent al constructor
        uic.loadUi('src_ui/menuRealizarComparacion.ui', self)
        self.conectar_bd()
        self.configurar_tabla()
        self.configurar_label_clickeable()
        self.personalizar_tableview()
        self.show()
        
    # Labels o elementos clickeables    
    def configurar_label_clickeable(self):
        self.labelVolverInicio.setCursor(Qt.CursorShape.PointingHandCursor)
        self.tableViewVerPerfiles.setModel(self.model)
        self.labelVolverInicio.mousePressEvent = self.abrir_ventana_menu_principal
        self.labelConfiguracion.mousePressEvent = self.abrir_ventana_menu_configuracion
        self.labelRealizarComparacion.mousePressEvent = self.comparar
    
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

    def comparar(self, *args):
        # Rutas de las carpetas de curriculums temporales y definitivos.
        rutaCarpetaCurriculumsTemporales = "cvsTemporales" 
        rutaCarpetaCurriculumsDefinitivos = "cvsDefinitivos" 
        id_seleccionado_para_comparar = (self.lineEditIdPerfilComparar.text().strip())
        id_existe = existe_id_perfil(id_seleccionado_para_comparar)
        umbral_seleccionado = float(self.comboBoxUmbralComparacion.currentText().strip())

        if id_existe:
            id_seleccionado_para_comparar = int(id_seleccionado_para_comparar)
            perfil = obtener_perfil_por_id(id_seleccionado_para_comparar)
            diccionario_con_rutas_y_textos_limpiados = generar_diccionario_textos(rutaCarpetaCurriculumsTemporales)
            resultados_primera_fase = comparar_curriculums(diccionario_con_rutas_y_textos_limpiados, perfil, umbral_seleccionado)
            print(mostrarResultadosTrasComparacion(resultados_primera_fase))
            moverCurriculumsTemporalesADefinitivos(resultados_primera_fase, rutaCarpetaCurriculumsTemporales, rutaCarpetaCurriculumsDefinitivos)
            # Comienza la inserción de los resultados en la base de datos tras la comparación.
            datos_perfil = obtener_perfil_por_id_para_insertar_en_resultados(id_seleccionado_para_comparar)
            insertar_resultados_comparacion(resultados_primera_fase, rutaCarpetaCurriculumsDefinitivos, datos_perfil, id_seleccionado_para_comparar)
            print("Puede consultar la tabla de resultados para información más detallada.")
            QMessageBox.information(self, "Éxito", "comparación realizada de manera exitosa. Consulte la ventana de resultados.")
            self.model.select() # Actualizamos el modelo para reflejar los cambios en la tabla.
            self.lineEditIdPerfilComparar.clear()
            
        elif not id_seleccionado_para_comparar:
            QMessageBox.warning(self, "Advertencia", "Por favor, ingrese un ID de perfil para comparar.")
            return
        elif id_seleccionado_para_comparar.isdigit() == False:
            QMessageBox.warning(self, "Advertencia", "El ID del perfil debe ser un número entero.")
            return
        
        elif not id_existe:
            QMessageBox.warning(self, "Advertencia", f"No existe un perfil con el ID {id_seleccionado_para_comparar}.")
            return

    # Funciones para conectar a la base de datos y configurar la tabla y ver los pefiles.
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
    ventana = VentanaMenuComparacion()
    sys.exit(app.exec())