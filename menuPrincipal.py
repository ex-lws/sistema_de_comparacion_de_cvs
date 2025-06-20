# menuPrincipal.py (modificado)
import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt
from src_old.GestorBD import *
from PyQt6.QtWidgets import QFileDialog, QApplication
import shutil
import os
import sys
from PyQt6.QtWidgets import QFileDialog, QMessageBox, QApplication

class VentanaMenuPrincipal(QtWidgets.QMainWindow):
    def __init__(self, parent):
        # Creamos la base de datos y las tablas si no existen.
        # Esto se hace una sola vez al iniciar la aplicación.
        crearBD()
        crearTabla()
        crearTablaResultados()
        # Flujo normal de la aplicación.
        # Inicializamos la ventana principal.
        self.parent = parent
        super().__init__()
        uic.loadUi('src_ui/menuPrincipal.ui', self)
        self.configurar_label_clickeable()
        self.show()
    
    # Labels clckeables y sus funciones asociadas.
    def configurar_label_clickeable(self):
        self.labelAnadiPerfiles.setCursor(Qt.CursorShape.PointingHandCursor)
        self.labelAnadiPerfiles.mousePressEvent = self.abrir_ventana_agregar_perfil
        self.labelVerPerfiles.setCursor(Qt.CursorShape.PointingHandCursor)
        self.labelVerPerfiles.mousePressEvent = self.abrir_ventana_ver_perfiles
        self.labelVerResultados.setCursor(Qt.CursorShape.PointingHandCursor)
        self.labelVerResultados.mousePressEvent = self.abrir_ventana_ver_resultados
        self.labelConfiguracion.mousePressEvent = self.abrir_ventana_menu_configuracion
        self.labelSubirCurriculum.mousePressEvent = self.seleccionar_y_subir_archivos
        self.labelEliminarPerfiles.mousePressEvent = self.abrir_ventana_menu_eliminar_perfiles
    
    # Funciones.
    def abrir_ventana_agregar_perfil(self, event):
        from menuAgregarPerfil import VentanaMenuAgregarPerfil
        
        self.ventana_agregar = VentanaMenuAgregarPerfil(self)  # Pasamos self como parent
        self.ventana_agregar.show()
        self.hide()  # Ocultamos la ventana principal

    def abrir_ventana_ver_perfiles(self, event):
        from menuVerPerfiles import VentanaMenuVerPefiles
        
        self.ventana_ver = VentanaMenuVerPefiles(self)
        self.ventana_ver.show()
        self.hide()

    def abrir_ventana_ver_resultados(self, event):
        from menuVerResultados import VentanaMenuVerResultados
        
        self.ventana_ver_resultados = VentanaMenuVerResultados(self)
        self.ventana_ver_resultados.show()
        self.hide()

    def abrir_ventana_menu_configuracion(self, event):
        from menuConfiguracion import VentanaMenuConfiguracion
        
        self.ventana_menu = VentanaMenuConfiguracion(self)
        self.ventana_menu.show()
        self.hide()

    def seleccionar_y_subir_archivos(self, event):
        ruta_cvs_temporales = 'cvsTemporales'
        app = QApplication.instance() or QApplication(sys.argv)
        archivos, _ = QFileDialog.getOpenFileNames(
            self,
            "Selecciona archivos PDF",
            "",
            "PDF Files (*.pdf)"
        )
        for archivo in archivos:
            if os.path.isfile(archivo):
                if archivo.lower().endswith('.pdf'):
                    shutil.copy(archivo, ruta_cvs_temporales)
                    print(f"Archivo copiado: {archivo} -> {ruta_cvs_temporales}")
                else:
                    QMessageBox.warning(
                        self,
                        "Archivo inválido",
                        f"El archivo '{os.path.basename(archivo)}' no es un PDF. Solo se permiten archivos .pdf."
                    )

    def abrir_ventana_menu_eliminar_perfiles(self, event):
        from menuEliminarPerfiles import VentanaMenuEliminarPefiles
        
        self.ventana_menu = VentanaMenuEliminarPefiles(self)
        self.ventana_menu.show()
        self.hide() 
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ventanaMenuPrincipal = VentanaMenuPrincipal(None)  # Pasamos None como parent inicial
    sys.exit(app.exec())