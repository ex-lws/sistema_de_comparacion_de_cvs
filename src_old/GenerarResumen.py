# EXPLICACIÓN: 
# Este código permite recoger los datos necesarios para dar de alta un resultado.
# Las variables se guardan en Python para después ser insertadas con otro método en la BD (Resultados).

# VERSIÓN:
# Versión 1.5 del código. 5/06/2025.

# Campos que requiere la talba de resultados.

# idResultado
# nombreCandidato
# porcentajeSimilitud
# puestoTrabajo -- Proviene de perfiles BD
# resumen
# pdfCurriculum
# nombrePerfil -- Proviene de perfiles BD
# idPerfil -- Proviene de perfiles BD

# Librerias necesarias

import os
import re
from pdfminer.high_level import extract_text
from sentence_transformers import SentenceTransformer, util

# 1. Extraer texto del PDF
def extraer_texto_pdf(ruta_pdf):
    return extract_text(ruta_pdf)

# 2. Dividir el texto en oraciones
def dividir_en_oraciones(texto):
    oraciones = re.split(r'(?<=[.!?]) +', texto)
    return [o.strip() for o in oraciones if len(o.strip()) > 20]

# 3. Obtener resumen usando sentence-transformers
modelo = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def obtener_resumen(texto, num_oraciones=5):
    oraciones = dividir_en_oraciones(texto)
    if len(oraciones) <= num_oraciones:
        return ' '.join(oraciones)

    embeddings = modelo.encode(oraciones, convert_to_tensor=True)
    centroide = embeddings.mean(dim=0)
    similitudes = util.cos_sim(embeddings, centroide)

    indices_top = similitudes.squeeze().argsort(descending=True)[:num_oraciones]
    resumen_ordenado = [oraciones[i] for i in sorted(indices_top.tolist())]
    return ' '.join(resumen_ordenado)

# 4. Procesar e imprimir
def procesar_cv(ruta_pdf):
    nombre_archivo = os.path.basename(ruta_pdf)
    texto = extraer_texto_pdf(ruta_pdf)
    resumen = obtener_resumen(texto)
    # Aquí ya puedes usarlo para insertar en la tabla
    return resumen


