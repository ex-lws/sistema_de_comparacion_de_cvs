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
from src_old.ActualizarPerfil import recabarIdParaEditarPerfil
from src_old.RealizarComparacion import *
from src_old.AccionesCurriculum import *
from src_old.SeleccionarPerfil import *
from src_old.GenerarResumen import *
from src_old.EliminarPerfiles import recabarIdParaEliminarPerfil

# Variables globales
# Ruta de la carpeta de curriculums temporales
rutaCarpetaCurriculumsTemporales = "cvsTermporales"  # Cambia por tu ruta real
rutaCarpetaCurriculumsDefinitivos = "cvsDefinitivos"  # Cambia por tu ruta real


def main():

    # INICA EL FLUJO IDEAL DEL PROGRAMA EN CONSOLA

    # 1.- Crear si no existe ya la base de datos y sus tablas.
    #verPerfiles()


    '''
    verPerfiles()
    parametros = recabarDatos()
    insertarPerfil(parametros)
    verPerfiles()
    texto = extraerTexto(rutaCarpetaCurriculumsTemporales)
    limpiar_texto(texto)
    diccionarioTrasLimpieza = generar_diccionario_textos(rutaCarpetaCurriculumsTemporales)
    idPerfil = recabarIdParaSeleccionarPerfil() 
    perfil = obtener_perfil_por_id(idPerfil)
    print(perfil)
    print ("Mostrar resultados de la comparación...")
    resultadosComparacion = comparar_curriculums(diccionarioTrasLimpieza, perfil["nombrePerfil"])
    mostrarResultadosTrasComparacion(resultadosComparacion)
    moverCurriculumsTemporalesADefinitivos(resultadosComparacion, rutaCarpetaCurriculumsTemporales, rutaCarpetaCurriculumsDefinitivos)
    print ("Los CVS temporales han sido movidos a la carpeta definitiva.")
    insertar_resultados_comparacion(
    resultadosComparacion,
    rutaCarpetaCurriculumsDefinitivos,
    perfil,
    RUTA_BD
    )
    '''

    seleccionUsuario = 0

    while (seleccionUsuario != 7):
        crearBD()
        crearTabla()
        crearTablaResultados()
        print("\n--- SISTEMA DE COMPARACIÓN DE CVS Y PERFILES DE TRABAJO ---")
        print("\nOpciones disponibles: ")
        print("1. Agregar un perfil")
        print("2. Realizar una comparación")
        print("3. Mostrar perfiles dados de alta")
        print("4. Editar perfiles")
        print("5. Eliminar perfiles")
        print("6. Subir curriculums")
        print("7. Consultar resultados")
        print("8. Salir")
        seleccionUsuario = int(input("\nSelecciona una opción: "))

        if seleccionUsuario == 1:
            print('--- Perfil agregado ---')
            parametros = recabarDatos()
            insertarPerfil(parametros)
        elif seleccionUsuario == 2:
            verPerfiles()
            texto = extraerTexto(rutaCarpetaCurriculumsTemporales)
            limpiar_texto(texto)
            diccionarioTrasLimpieza = generar_diccionario_textos(rutaCarpetaCurriculumsTemporales)
            idPerfil = recabarIdParaSeleccionarPerfil() 
            perfil = obtener_perfil_por_id(idPerfil)
            print(perfil)
            print ("Mostrar resultados de la comparación...")
            resultadosComparacion = comparar_curriculums(diccionarioTrasLimpieza, perfil["nombrePerfil"])
            mostrarResultadosTrasComparacion(resultadosComparacion)
            moverCurriculumsTemporalesADefinitivos(resultadosComparacion, rutaCarpetaCurriculumsTemporales, rutaCarpetaCurriculumsDefinitivos)
            print ("Los CVS temporales han sido movidos a la carpeta definitiva.")
            insertar_resultados_comparacion(
            resultadosComparacion,
            rutaCarpetaCurriculumsDefinitivos,
            perfil,
            RUTA_BD
            )
        elif seleccionUsuario == 3:
            print('--- Mostrando los perfiles registrados ---')
            verPerfiles()
        elif seleccionUsuario == 4:
            print('--- Editar Perfiles ---')
            print("Selecciona el ID del perfil que deseas editar:")
            verPerfiles()
            idPerfil = recabarIdParaEditarPerfil()
            if idPerfil is not None:
                parametros = recabarDatos()
                modificarPerfil(idPerfil, parametros)
            else:
                print("No se pudo editar el perfil, ID no válido.")
        elif seleccionUsuario == 5:
            print('--- Eliminar Perfiles ---')
            print("Selecciona el ID del perfil que deseas eliminar:")
            verPerfiles()
            idPerfil = recabarIdParaEliminarPerfil()
            if idPerfil is not None:
                eliminarPerfil(idPerfil)
            else:
                print("No se pudo eliminar el perfil, ID no válido.")
        elif seleccionUsuario == 6:
            print('--- Subir Curriculums ---')
        elif seleccionUsuario == 7:
            print("Consultar Resultados...")
            verResultadosTabla()
        elif seleccionUsuario == 8:
            print('--- Saliendo del Programa ---')
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")
main()