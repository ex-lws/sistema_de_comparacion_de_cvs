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
from src_old.AgregarPerfil import *
from src_old.SeleccionarPerfilParaActualizar import recabarIdParaEditarPerfil
from src_old.RealizarComparacion import *
from src_old.AccionesCurriculum import *
from src_old.SeleccionarPerfilParaComparar import *
from src_old.GenerarResumen import *
from src_old.SeleccionarPerfilParaEliminar import recabarIdParaEliminarPerfil

# Variables globales
# Ruta de la carpeta de curriculums temporales
rutaCarpetaCurriculumsTemporales = "cvsTemporales"
rutaCarpetaCurriculumsDefinitivos = "cvsDefinitivos"  
RUTA_BD = Path('BD/Perfiles.bd')


def main():

    # INICA EL FLUJO IDEAL DEL PROGRAMA EN CONSOLA

    seleccionUsuario = 0

    while (seleccionUsuario != 7):
        crearBD()
        crearTabla()
        crearTablaResultados()
        print("\n--- SISTEMA DE COMPARACIÓN DE CVS Y PERFILES DE TRABAJO ---")
        print("\n***Favor de tener dentro de la carpeta cvsTemporales los curriculums que se desean comparar.***")
        print("\nOpciones disponibles: ")
        print("1. Agregar un perfil")
        print("2. Realizar una comparación")
        print("3. Mostrar perfiles dados de alta")
        print("4. Editar perfiles")
        print("5. Eliminar perfiles")
        print("6. Subir curriculums")
        print("7. Consultar resultados")
        print("8. Borrar todos los curriculums")
        print("9. Borrar todos los datos")
        print("10. Borrar todos los resultados")
        print("11. Salir")
        seleccionUsuario = int(input("\nSelecciona una opción: "))

        if seleccionUsuario == 1: # Agregar un perfil desde consola.
            print('--- Perfil agregado ---')
            parametros = recabarDatos()
            insertarPerfil(parametros)
            print("Perfil agregado exitosamente.")
        elif seleccionUsuario == 2: # Realizar una compración entre curriculums y un perfil dado de alta.
            verPerfiles()
            print ('Seleccione un perfil por medio de un ID para comenzaar con la comparación:')
            id_seleccionado_por_el_usuario = recabarIdParaSeleccionarPerfil()
            # Una vez se tiene el ID seleccionado por el usuario, se procede a extraer el perfil de la base de datos.
            # Primero comprobar si el ID es valido.
            if existe_id_perfil(id_seleccionado_por_el_usuario):
                print(f"ID {id_seleccionado_por_el_usuario} es válido, procediendo a extraer el perfil...")
                perfil_extraido = obtener_perfil_por_id(id_seleccionado_por_el_usuario)
            else:
                print(f"ID {id_seleccionado_por_el_usuario} no es válido, por favor intenta de nuevo.")
                continue
            # Una vez se tiene el perfil, se procede a realizar la comparación.
            # Se comienza con la extracción y limpieza de los textos de los curriculums temporales.
            # Este método embebe la extracción de texto de los PDFs y su limpieza.
            print("Extrayendo y limpiando textos de los curriculums temporales...")
            diccionario_con_rutas_y_textos_limpiados = generar_diccionario_textos(rutaCarpetaCurriculumsTemporales)
            # Comienza el proces de comparación.
            resultados_primera_fase = comparar_curriculums(diccionario_con_rutas_y_textos_limpiados, perfil_extraido)
            # Mostrar los resultados de la comparación en la primera fase.
            print(mostrarResultadosTrasComparacion(resultados_primera_fase))
            #Comienza el movimiento de los curriculums temporales a los definitivos.
            moverCurriculumsTemporalesADefinitivos(resultados_primera_fase, rutaCarpetaCurriculumsTemporales, rutaCarpetaCurriculumsDefinitivos)
            print("Curriculums movidos a la carpeta de curriculums definitivos.")
            # Comienza la inserción de los resultados en la base de datos tras la comparación.
            datos_perfil = obtener_perfil_por_id_para_insertar_en_resultados(id_seleccionado_por_el_usuario)
            insertar_resultados_comparacion(resultados_primera_fase, rutaCarpetaCurriculumsDefinitivos, datos_perfil, id_seleccionado_por_el_usuario)
            print("Puede consultar la tabla de resultados para información más detallada.")

        elif seleccionUsuario == 3: # Mostrar perfiles dados de alta.
            print('--- Mostrando los perfiles registrados ---')
            verPerfiles()
        elif seleccionUsuario == 4: # Editar perfiles.
            print('--- Editar Perfiles ---')
            print("Selecciona el ID del perfil que deseas editar:")
            verPerfiles()
            idPerfil = recabarIdParaEditarPerfil()
            if idPerfil is not None:
                parametros = recabarDatos()
                modificarPerfil(idPerfil, parametros)
            else:
                print("No se pudo editar el perfil, ID no válido.")
        elif seleccionUsuario == 5: # Eliminar perfiles.
            print('--- Eliminar Perfiles ---')
            print("Selecciona el ID del perfil que deseas eliminar:")
            verPerfiles()
            idPerfil = recabarIdParaEliminarPerfil()
            if idPerfil is not None:
                eliminarPerfil(idPerfil)
            else:
                print("No se pudo eliminar el perfil, ID no válido.")
        elif seleccionUsuario == 6: # Método agregado desde el front end.
            print('--- Subir Curriculums ---')
        elif seleccionUsuario == 7:
            print("Consultar Resultados...")
            verResultadosTabla()
        elif seleccionUsuario == 8: # Borrar todos los CVS.
            print('--- Borrar todos los curriculums ---')
            borrar_todos_los_archivos(rutaCarpetaCurriculumsTemporales)
            borrar_todos_los_archivos(rutaCarpetaCurriculumsDefinitivos)
        elif seleccionUsuario == 9: # Borrar la base de datos.
            print('--- Borrar todos los datos ---')
            borrarBD()
        elif seleccionUsuario == 10:
            print("Borrando resultados...")
            borrarTablaResultados()
            print("Los resultados han sido borrados.")
        elif seleccionUsuario == 11: # Salir del programa.
            print('--- Saliendo del Programa ---')
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")
main()