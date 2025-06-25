# EXPLICACIÓN: 
# Este código permite poder generar un resumen a partir de los CVS definitivos.
# La variable resumen es necesaria para poder insertarla dentro de la tabla de Resultados.
# Generar el resumen requiere de extrer el texto y limpiarlo, por lo que se quiere importar métodos de AccionesCurriculum.py
# Por otro lado, estos métodos embebidos deberán funcionar con la ruta de los CVS definitivos. (Aquellos que pasaron la prueba.)

# VERSIÓN:
# Versión 1.6 del código. 25/06/2025.

# Librerias necesarias
import os
import re
from pdfminer.high_level import extract_text
from sentence_transformers import SentenceTransformer, util
from src_old.AccionesCurriculum import *

# Modelo de SentenceTransformer para generar embeddings.
modelo = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Dividir el texto en oraciones.
def dividir_en_oraciones(texto_limpiado):
    oraciones = re.split(r'(?<=[.!?]) +', texto_limpiado)
    return [o.strip() for o in oraciones if len(o.strip()) > 20]

# Generar un resumen de texto.
def obtener_resumen(num_oraciones=5):
    rutaCarpetaCurriculumsDefinitivos = "cvsDefinitivos"  
    texto_extraido = extraerTexto(rutaCarpetaCurriculumsDefinitivos)    
    texto_limpiado = limpiar_texto(texto_extraido)
    oraciones = dividir_en_oraciones(texto_limpiado)
    if len(oraciones) <= num_oraciones:
        return ' '.join(oraciones)

    embeddings = modelo.encode(oraciones, convert_to_tensor=True)
    centroide = embeddings.mean(dim=0)
    similitudes = util.cos_sim(embeddings, centroide)

    indices_top = similitudes.squeeze().argsort(descending=True)[:num_oraciones]
    resumen_ordenado = [oraciones[i] for i in sorted(indices_top.tolist())]
    return ' '.join(resumen_ordenado)

# Imprimir el resumen en consola.
def procesar_cv(ruta_pdf):
    nombre_archivo = os.path.basename(ruta_pdf)
    resumen = obtener_resumen()
    # Aquí ya puedes usarlo para insertar en la tabla
    return resumen


