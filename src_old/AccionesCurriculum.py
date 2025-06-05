# EXPLICACIÓN: 
# Este código permite realizar las diferentes acciones de movimientos de PDFS (CVS) dentro del sistema.

# VERSIÓN:
# Versión 1.5 del código. 05/06/2025.

# Importar las librerías necesarias

#NOTA: 
# Estos métodos requieren de returns de otros métodos para poder funcionar
# Llamar desde el main siguiendo el flujo del programa.

import os
import re
from pdfminer.high_level import extract_text 

# Variables globales
# Ruta de la carpeta de curriculums temporales
rutaCarpetaCurriculumsTemporales = "cvsTermporales"  # Cambia por tu ruta real
rutaCarpetaCurriculumsDefinitivos = "cvsDefinitivos"  # Cambia por tu ruta real

# Extrae el texto de un PDF y lo guarda en una variable
def extraerTexto(rutaCarpetaCurriculumsTemporales):
    try:
        text = extract_text(rutaCarpetaCurriculumsTemporales).upper()
        text = limpiar_texto(text)
        return text
    except Exception as e:
        return f"ERROR, NO HA SIDO POSIBLE EXTRAER EL TEXTO DEL PDF... : {str(e)}"
    
# Limpiar texto
def limpiar_texto(texto):
    """
    Limpia el texto eliminando saltos de línea, espacios extra y caracteres no deseados.
    """
    #texto = texto.replace('\n', ' ')           # Quita saltos de línea
    #texto = texto.replace('\r', ' ')           # Quita retornos de carro
    texto = re.sub(r'\s+', ' ', texto)         # Reemplaza múltiples espacios por uno solo
    texto = re.sub(r'[^\w\s.,;:!?()\-]', '', texto)  # Quita caracteres especiales no deseados
    texto = texto.strip()                      # Quita espacios al inicio y final
    return texto


# Generar diccionario con las rutas relativas y el texto extraído para su posterior uso en la comparacion
def generar_diccionario_textos(rutaCarpetaCurriculumsTemporales):
    diccionario_final = {} # Contendra keys (rutas relativas) y values (textos extraidos)
    
    for raiz, _, archivos in os.walk(rutaCarpetaCurriculumsTemporales):
        for archivo in archivos:
            if archivo.lower().endswith('.pdf'):
                ruta_relativa = os.path.relpath(os.path.join(raiz, archivo), rutaCarpetaCurriculumsTemporales)
                ruta_absoluta = os.path.join(rutaCarpetaCurriculumsTemporales, ruta_relativa)
                # Extraer texto del PDF
                texto_extraido = extraerTexto(ruta_absoluta)
                diccionario_final[ruta_relativa] = texto_extraido
    
    return diccionario_final

# Tras la limpieza genera un txt en pro de mejorar el rendimiento del programa.
def generartxt(diccionario_final, rutaCarpetaCurriculumsTemporales):
    """
    Genera un archivo de texto con el contenido del diccionario.
    """
    ruta_txt = os.path.join(rutaCarpetaCurriculumsDefinitivos, "curriculums.txt")
    
    with open(ruta_txt, 'w', encoding='utf-8') as f:
        for ruta, texto in diccionario_final.items():
            f.write(f"RUTA: {ruta}\n")
            f.write(f"TEXTO: {texto}\n\n")
    
    print(f"Archivo de texto generado en: {ruta_txt}")

def mostrarResultadosTrasComparacion (resultados):
    for ruta, texto in resultados.items():
        print(f"\n📄 **RUTA RELATIVA: {ruta}**...")
        print(f"**TEXTO EXTRAIDO: {texto[:20000]}**...")  # Muestra los primeros 200 caracteres






