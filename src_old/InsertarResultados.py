import sqlite3
import os
from src_old.Obtener3datosdeperfiles import *
from src_old.AgregarResultados import *

def extraer_nombre_candidato(nombre_archivo):
    # Asume que el nombre es algo como: "CV_JUAN PÉREZ_MARKETING.pdf"
    base = os.path.basename(nombre_archivo)
    nombre = os.path.splitext(base)[0]
    nombre = nombre.replace("CV_", "").replace("_", " ").strip()
    return nombre

def insertar_resultados_comparacion(resultadosComparacion, ruta_definitiva, perfil, ruta_bd):
    for nombre_archivo, porcentaje_similitud in resultadosComparacion.items():
        ruta_pdf = os.path.join(ruta_definitiva, os.path.basename(nombre_archivo))

        # Extraer valores
        nombre_candidato = extraer_nombre_candidato(nombre_archivo)
        texto = extraer_texto_pdf(ruta_pdf)
        resumen = obtener_resumen(texto)

        with open(ruta_pdf, "rb") as f:
            pdf_bytes = f.read()

        # Insertar en la tabla Resultados
        conn = sqlite3.connect(ruta_bd)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Resultados (
                nombreCandidato, porcentajeSimilitud, puestoTrabajo, resumen, pdfCurriculum, nombrePefil, idPerfil
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            nombre_candidato,
            porcentaje_similitud,
            perfil["puestoTrabajo"],
            resumen,
            pdf_bytes,
            perfil["nombrePerfil"],
            perfil["id"]
        ))
        conn.commit()
        conn.close()
