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

# Variables globales
# Ruta de la carpeta de curriculums temporales
rutaCarpetaCurriculumsTemporales = "cvsTermporales"  # Cambia por tu ruta real
rutaCarpetaCurriculumsDefinitivos = "cvsDefinitivos"  # Cambia por tu ruta real


def main():

    # INICA EL FLUJO IDEAL DEL PROGRAMA EN CONSOLA

    # 1.- Crear si no existe ya la base de datos y sus tablas.
    #verPerfiles()
    '''
    crearBD()
    crearTabla()
    crearTablaResultados()
    verPerfiles()
    parametros = recabarDatos()
    insertarPerfil(parametros)
    '''
    verPerfiles()
    texto = extraerTexto(rutaCarpetaCurriculumsTemporales)
    limpiar_texto(texto)
    diccionarioTrasLimpieza = generar_diccionario_textos(rutaCarpetaCurriculumsTemporales)
    idPerfil = recabarIdParaSeleccionarPerfil() 
    perfil = obtener_perfil_por_id(idPerfil)
    print(perfil)
    print ("Mostrar resultados de la comparación...")
    resultadosComparacion = comparar_curriculums(diccionarioTrasLimpieza, perfil["nombrePerfil"])
    # Tras la comparación se puede ingestar si existe la variable en la tabla resultados.
    mostrarResultadosTrasComparacion(resultadosComparacion)
    moverCurriculumsTemporalesADefinitivos(resultadosComparacion, rutaCarpetaCurriculumsTemporales, rutaCarpetaCurriculumsDefinitivos)
    print ("Los CVS temporales han sido movidos a la carpeta definitiva.")
    insertar_resultados_comparacion(
    resultadosComparacion,
    rutaCarpetaCurriculumsDefinitivos,
    perfil,
    RUTA_BD  # o el path a tu base de datos
    )
    verResultadosTabla()
main()