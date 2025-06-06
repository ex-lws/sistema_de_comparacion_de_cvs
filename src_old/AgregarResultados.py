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
import sqlite3
import os

def insertar_resultados(resultados_dict, idPerfil):
    perfil = obtener_perfil_por_id(idPerfil)
    if not perfil:
        return

    nombrePerfil = perfil[1]  # nombrePerfil
    puestoTrabajo = perfil[9]  # puestoTrabajo

    conexion = sqlite3.connect(RUTA_BD)
    conexion.execute("PRAGMA foreign_keys = ON")
    cursor = conexion.cursor()

    for ruta, similitud in resultados_dict.items():
        nombre_candidato = extraer_nombre_desde_ruta(ruta)  # tu función personalizada
        resumen = f"CV con similitud del {similitud:.2f} %"
        pdf_blob = leer_pdf_como_blob(ruta)  # ver función abajo

        cursor.execute('''
            INSERT INTO Resultados (
                nombreCandidato,
                porcentajeSimilitud,
                puestoTrabajo,
                resumen,
                pdfCurriculum,
                nombrePefil,
                idPerfil
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            nombre_candidato,
            f"{similitud:.2f} %",
            puestoTrabajo,
            resumen,
            pdf_blob,
            nombrePerfil,
            idPerfil
        ))

    conexion.commit()
    conexion.close()

def leer_pdf_como_blob(ruta):
    with open(ruta, 'rb') as file:
        return file.read()

def extraer_nombre_desde_ruta(ruta):
    nombre_archivo = os.path.basename(ruta)
    nombre = nombre_archivo.replace("CV_", "").replace(".pdf", "").strip()
    return nombre
