# Esta clase tiene la responsabilidad de hacer multiples acciones en los curriculums.
# Version 1.0

from pdfminer.high_level import extract_text
import os


nombreCarpeta = "cvsTermporales"
def extraerRutasRelativas(nombreCarpeta):
    return {
        os.path.relpath(os.path.join(raiz, archivo), nombreCarpeta): True  # Valor arbitrario (puede ser 1, None, etc.)
        for raiz, _, archivos in os.walk(nombreCarpeta)
        for archivo in archivos
        if archivo.lower().endswith('.pdf')
    }


ruta = "C:\\Users\\agell\\Downloads\\CV_HUGO GÓMEZ VILLAREAL _SUPPLY CHAIN.pdf"
def extraerTexto(ruta):
    text = extract_text(ruta)
    print(text.upper())



diccionario_prueba = extraerRutasRelativas(nombreCarpeta)
print(diccionario_prueba)
#extraerTexto(ruta)