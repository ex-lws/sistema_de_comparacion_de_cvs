# En esta clase se harán las pruebas del sistema en su versión de consola. 

# Clases importatdas

from src_old.GestorBD import *
from src_old.AgregarPerfil import recabarDatos


def main():
    crearBD()
    crearTabla()
    datos = recabarDatos()
    insertarPerfil(datos)
    print ("Perfil agregado correctamente.")
    verPerfiles()

main()