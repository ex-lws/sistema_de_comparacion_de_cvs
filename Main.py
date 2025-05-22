# En esta clase se harán las pruebas del sistema en su versión de consola. 

# Clases importatdas

from src_old.GestorBD import *
from src_old.AgregarPerfil import recabarDatos

from src_old.ActualizarPerfil import recabarIdParaEditarPerfil


def main():
    # Crear la base de datos y la tabla
    crearBD()
    crearTabla()

    # Recabar datos para insertar un perfil en la base de datos
    #datos = recabarDatos()
    #insertarPerfil(datos)

    # Ver todos los perfiles
    #verPerfiles()

    # Recabar el ID del perfil a eliminar y eliminarlo
    #id = recabarIdParaEliminarPerfil()
    #eliminarPerfil(id)
    #verPerfiles()

    # Recabar el ID del perfil a editar y los actualizar nuevos datos
    #verPerfiles()
    #id = recabarIdParaEditarPerfil()
    #datos = recabarDatos()
    #modificarPerfil(id, datos)
    #verPerfiles()


main()