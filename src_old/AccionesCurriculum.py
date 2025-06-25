# EXPLICACIÓN: 
# Este código permite realizar las diferentes acciones de movimientos de PDFS (CVS) dentro del sistema.

# VERSIÓN:
# Versión 1.7 del código. 25/06/2025.

# Importar las librerías necesarias
import os
import re
from pdfminer.high_level import extract_text 

# Variables globales
# Ruta de la carpeta de curriculums temporales
rutaCarpetaCurriculumsTemporales = "cvsTemporales" 
rutaCarpetaCurriculumsDefinitivos = "cvsDefinitivos" 

# Extrae el texto de un PDF y lo guarda en una variable.
# Requiere de la ruta de los curriculums temporales.
def extraerTexto(rutaCarpetaCurriculumsTemporales):
    try:
        text = extract_text(rutaCarpetaCurriculumsTemporales).upper()
        text = limpiar_texto(text)
        return text
    except Exception as e:
        return f"ERROR, NO HA SIDO POSIBLE EXTRAER EL TEXTO DEL PDF... : {str(e)}"
    
# Limpiar texto extraído de un PDF y lo guarda en una variable.
# Requiere de la variable texto que es el texto extraído del PDF.
def limpiar_texto(texto):
    """
    Limpia el texto eliminando saltos de línea, espacios extra y caracteres no deseados.
    """
    #texto = texto.replace('\n', ' ')
    #texto = texto.replace('\r', ' ')          
    texto = re.sub(r'\s+', ' ', texto)         
    texto = re.sub(r'[^\w\s.,;:!?()\-]', '', texto)  
    texto = texto.strip()                      
    return texto


# Generar diccionario con las rutas relativas y el texto extraído, limpiado para su posterior uso en la comparacion.
# Requiere como parametro la ruta de la carpeta de curriculums temporales.
# Esta función tiene métodos embebidos que iteran por cada elementos de la carpeta de curriculums temporales.
# Se extrae el texto, se limpia y se guarda en un diccionario con la ruta relativa como clave y el texto limpio como valor.
# Sólo lo hace con los archivos PDF, ignorando otros tipos de archivos.
# Básicamente, este diccionario contiene las rutas de los cvs temporales y el texto extraído de cada uno de ellos.
def generar_diccionario_textos(rutaCarpetaCurriculumsTemporales):
    diccionario_semi_final = {}
    
    for raiz, _, archivos in os.walk(rutaCarpetaCurriculumsTemporales):
        for archivo in archivos:
            if archivo.lower().endswith('.pdf'):
                ruta_relativa = os.path.relpath(os.path.join(raiz, archivo), rutaCarpetaCurriculumsTemporales)
                ruta_absoluta = os.path.join(rutaCarpetaCurriculumsTemporales, ruta_relativa)
                texto_extraido = extraerTexto(ruta_absoluta)
                texto_limpiado = limpiar_texto(texto_extraido)
                diccionario_semi_final[ruta_relativa] = texto_limpiado
    
    return diccionario_semi_final

# Mover los curriculums temporales a definitivos, es decir, aquellos que han pasado la comparacion.
# Requerimos de la variable resultados que es un diccionario posterior a la comparacion de los curriculums y las rutas globales de las carpetas.
def moverCurriculumsTemporalesADefinitivos(diccionario_resultados, rutaCarpetaCurriculumsTemporales, rutaCarpetaCurriculumsDefinitivos):
    """
    Mueve los archivos PDF de la carpeta temporal a la carpeta definitiva,
    solo para las rutas presentes en el diccionario_resultados.
    """
    if not os.path.exists(rutaCarpetaCurriculumsDefinitivos):
        os.makedirs(rutaCarpetaCurriculumsDefinitivos)

    for ruta_relativa in diccionario_resultados.keys():
        ruta_origen = os.path.join(rutaCarpetaCurriculumsTemporales, ruta_relativa)
        ruta_destino = os.path.join(rutaCarpetaCurriculumsDefinitivos, os.path.basename(ruta_relativa))
        if os.path.exists(ruta_origen):
            os.rename(ruta_origen, ruta_destino)
            print(f"Movido: {ruta_relativa} a {rutaCarpetaCurriculumsDefinitivos}")
        else:
            print(f"No encontrado: {ruta_origen}")

# Borrar todos los archivos, pasandole como parametro de la ruta especificada.
# Funciona tanto para la carpeta de curriculums temporales como para la de definitivos.
def borrar_todos_los_archivos(ruta_carpeta):
    """
    Borra todos los archivos de la carpeta especificada.
    """
    if os.path.exists(ruta_carpeta):
        for archivo in os.listdir(ruta_carpeta):
            ruta_archivo = os.path.join(ruta_carpeta, archivo)
            if os.path.isfile(ruta_archivo):
                try:
                    os.remove(ruta_archivo)
                    print(f"Borrado: {ruta_archivo}")
                except Exception as e:
                    print(f"Error al borrar {ruta_archivo}: {e}")
    else:
        print(f"La carpeta {ruta_carpeta} no existe.")


    
