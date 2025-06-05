# EXPLICACIÓN: 
# Este código permite realizar todas las acciones del sistema en su versión de consola.

# VERSIÓN:
# Versión 1.5 del código. 05/06/2025.

# Importar las librerías necesarias

#NOTA: 
# Estos métodos requieren de returns de otros métodos para poder funcionar
# Seguir siempre el correcto flujo del programa


# Clases necesarias para funcionar
from src_old.GestorBD import *
from src_old.AgregarPerfil import recabarDatos
from src_old.ActualizarPerfil import recabarIdParaEditarPerfil
from src_old.RealizarComparacion import *
from src_old.AccionesCurriculum import *
from src_old.SeleccionarPerfil import *


def main():
    # INICA EL FLUJO IDEAL DEL PROGRAMA EN CONSOLA

    # 1.- Crear si no existe ya la base de datos y sus tablas.
    # 2.- Mostrar las diferentes opciones del sistema al usuario y perdir la elección de una.
    # 3.- Agregar un perfil. (Recoger datos y darlo de alta en la BD (Perfiles))
    # 4.- Agregar un CV (Permite subir un CV y realizar la extracción de texto, limpieza y optimización).
    # 5.- Seleccionar un perfil que se usará para la comparación.
    # 6.- Comparar CV vs pefil (Muestra resultados únicamente de aquellos con un 80% de simulitud).
    # (Movimiento de CVS temporales a definitivos y eliminacion de todos los CVS temporales en dicha carpeta).
    # 7.- Guardar los resultados en la BD (Resultados).
    # 8.- Permitir elimianar un perfil.
    # 9.- Permitir actualizar un perfil.
    # 10.- Permitir poder consultar los resultados (consulta SQL de la tabla Resultados).

    # INCIA LA LLAMADA DE METODOS:
    
    # Crear la base de datos y la tabla
    crearBD()
    crearTabla()
    crearTablaResultados()

    # Recabar datos para insertar un perfil en la base de datos
    datos = recabarDatos()
    insertarPerfil(datos)

    # Ver todos los perfiles
    verPerfiles()

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
    #id = recabarIdParaSeleccionarPerfil()
    #perfilEncontrado = str(obtener_perfil_por_id(id))
    #curriculums= generar_diccionario_textos(rutaCarpetaCurriculumsTemporales)
    #resultados=comparar_curriculums(curriculums, perfilEncontrado)
    #print(resultados)


main()