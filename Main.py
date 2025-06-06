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
from src_old.AgregarResultados import *

# Variables globales
# Ruta de la carpeta de curriculums temporales
rutaCarpetaCurriculumsTemporales = "cvsTermporales"  # Cambia por tu ruta real
rutaCarpetaCurriculumsDefinitivos = "cvsDefinitivos"  # Cambia por tu ruta real


def main():
    # INICA EL FLUJO IDEAL DEL PROGRAMA EN CONSOLA

    # 1.- Crear si no existe ya la base de datos y sus tablas.
    verPerfiles()
    crearBD()
    crearTabla()
    crearTablaResultados()
    texto = extraerTexto(rutaCarpetaCurriculumsTemporales)
    limpiar_texto(texto)
    diccionarioTrasLimpieza = generar_diccionario_textos(rutaCarpetaCurriculumsTemporales)
    idPerfil = recabarIdParaSeleccionarPerfil() 
    perfil = obtener_perfil_por_id(idPerfil)
    print(perfil)
    print ("Mostrar resultados de la comparación...")
    resultadosComparacion = comparar_curriculums(diccionarioTrasLimpieza, perfil)
    # Tras la comparación se puede ingestar si existe la variable en la tabla resultados.
    mostrarResultadosTrasComparacion(resultadosComparacion)
    moverCurriculumsTemporalesADefinitivos(resultadosComparacion, rutaCarpetaCurriculumsTemporales, rutaCarpetaCurriculumsDefinitivos)
    print ("Los CVS temporales han sido movidos a la carpeta definitiva.")
    # Insertar resultados en la base de datos, en la tabla Resultados.
    verResultados()


    
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
    # 11.- Ver perfiles.

main()