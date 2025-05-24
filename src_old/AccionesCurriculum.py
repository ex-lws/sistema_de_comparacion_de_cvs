# Version 2.0 de las acciones respecto a los curriculums.

import os
from pdfminer.high_level import extract_text 

# Variables globales
# Ruta de la carpeta de curriculums temporales
rutaCarpetaCurriculumsTemporales = "cvsTermporales"  # Cambia por tu ruta real

# Extrae el texto de un PDF y lo guarda en una variable
def extraerTexto(rutaCarpetaCurriculumsTemporales):
    try:
        text = extract_text(rutaCarpetaCurriculumsTemporales).upper()
        return text
    except Exception as e:
        return f"ERROR, NO HA SIDO POSIBLE EXTRAER EL TEXTO DEL PDF... : {str(e)}"

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

# Prubeas de las funciones
resultados = generar_diccionario_textos(rutaCarpetaCurriculumsTemporales)
    
# Ejemplo: imprimir resultados
for ruta, texto in resultados.items():
    print(f"\n📄 **RUTA RELATIVA: {ruta}**...")
    print(f"**TEXTO EXTRAIDO: {texto[:20000]}**...")  # Muestra los primeros 200 caracteres