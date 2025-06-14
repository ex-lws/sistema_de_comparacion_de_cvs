# EXPLICACIÓN: 
# Este código permite realizar las diferentes acciones CRUD del sistema.

# VERSIÓN:
# Versión 1.5 del código. 05/06/2025.

# Importar las librerías necesarias

import sqlite3
from pathlib import Path
import os
from src_old.GenerarResumen import *

# Ruta de la base de datos en el proyecto.
RUTA_BD = Path('BD/Perfiles.bd')

def crearBD():
    # Crear carpeta si no existe
    RUTA_BD.parent.mkdir(exist_ok=True)
    # Conectar a la base de datos (se crea si no existe)
    conexion = sqlite3.connect(RUTA_BD)
    #print("Base de datos creada o ya existe.")
    conexion.close()

def crearTabla():
    # Crear un cursor para ejecutar comandos SQL
    conexion = sqlite3.connect(RUTA_BD)
    conexion.execute("PRAGMA foreign_keys = ON")  # Activa llaves foráneas
    cursor = conexion.cursor()
    # Crear la tabla de perfiles si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Perfiles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombrePerfil TEXT NOT NULL,
            tipoContratacion TEXT NOT NULL,
            horarioTrabajo TEXT NOT NULL,
            modalidadTrabajo TEXT NOT NULL,
            sueldoMensualMinimo DOUBLE NOT NULL,
            sueldoMensualMaximo DOUBLE NOT NULL,
            escolaridad TEXT NOT NULL,
            area TEXT NOT NULL,
            puestoTrabajo TEXT NOT NULL,
            ubicacion TEXT NOT NULL,
            idioma TEXT NOT NULL,
            nivelIdioma TEXT,
            licenciaConducir BOOLEAN NOT NULL,
            anosExperiencia INTEGER NOT NULL
        )
    ''')
    #print ("Tabla 'Perfiles' creada o ya existe.")
    # Guardar los cambios y cerrar la conexión
    conexion.commit()
    conexion.close()

def crearTablaResultados():
    # Crear un cursor para ejecutar comandos SQL
    conexion = sqlite3.connect(RUTA_BD)
    conexion.execute("PRAGMA foreign_keys = ON")  # Activa llaves foráneas
    cursor = conexion.cursor()
    # Crear la tabla de perfiles si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Resultados (
            idResultado INTEGER PRIMARY KEY AUTOINCREMENT,
            nombreCandidato TEXT NOT NULL,
            porcentajeSimilitud TEXT NOT NULL,
            puestoTrabajo TEXT NULL, -- Proviene de perfiles BD
            resumen TEXT NOT NULL,
            pdfCurriculum BLOP,
            nombrePefil NOT NULL, -- Proviene de perfiles BD
            idPerfil INTEGER NOT NULL, -- Proviene de perfiles BD 
            FOREIGN KEY (idPerfil) REFERENCES Perfiles(id)
        )
    ''')
    #print ("Tabla 'Resultados' creada o ya existe.")
    # Guardar los cambios y cerrar la conexión
    conexion.commit()
    conexion.close()

# Operaciones CRUD

# Ver todos los perfiles
def verPerfiles():
    conexion = sqlite3.connect(RUTA_BD)
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Perfiles")
    perfiles = cursor.fetchall()
    print ("Perfiles registrados:")
    # Imprimir los perfiles en consola
    for perfil in perfiles:
        print(perfil)
    conexion.close()

# Insertar perfiles (Requiere de previamente recoger los datos a insertar)
def insertarPerfil(parametros):
    conexion = sqlite3.connect(RUTA_BD)
    cursor = conexion.cursor()
    cursor.execute('''
        INSERT INTO Perfiles (
            nombrePerfil, tipoContratacion, horarioTrabajo, modalidadTrabajo, sueldoMensualMinimo,
            sueldoMensualMaximo, escolaridad, area, puestoTrabajo, ubicacion, idioma,
            nivelIdioma, licenciaConducir, anosExperiencia
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', parametros)
    conexion.commit()
    conexion.close()

# Eliminar un perfil por medio del ID. (Requiere de recoger un ID)
def eliminarPerfil(id):
    conexion = sqlite3.connect(RUTA_BD)
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM Perfiles WHERE id = ?", (id,))
    conexion.commit()
    conexion.close()
    print(f"Perfil con ID {id} eliminado.")

# Actualizar un perfil por medio del ID. (Requiere de recoger un ID y modificar parametros)
def modificarPerfil(id, parametros):
    conexion = sqlite3.connect(RUTA_BD)
    cursor = conexion.cursor()
    cursor.execute('''
        UPDATE Perfiles SET
            nombrePerfil = ?,
            tipoContratacion = ?,
            horarioTrabajo = ?,
            modalidadTrabajo = ?,
            sueldoMensualMinimo = ?,
            sueldoMensualMaximo = ?,
            escolaridad = ?,
            area = ?,
            puestoTrabajo = ?,
            ubicacion = ?,
            idioma = ?,
            nivelIdioma = ?,
            licenciaConducir = ?,
            anosExperiencia = ?
        WHERE id = ?
    ''', (*parametros, id))
    conexion.commit()
    conexion.close()
    print(f"Perfil con ID {id} modificado.")

# Seleccionar un perfil y guardarlo en una variable por medio de un select from id (Requiere de recabar el ID)
def obtener_perfil_por_id(id):
    conexion = sqlite3.connect(RUTA_BD)
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Perfiles WHERE id = ?", (id,))
    perfil = cursor.fetchone()
    conexion.close()
    
    if perfil:
        return perfil
    else:
        print(f"No se encontró un perfil con ID {id}.")
        return None
    
# Seleccionar un perfil y guardarlo en una variable por medio de un select from id (Requiere de recabar el ID)
def verResultadosTabla():
    conexion = sqlite3.connect(RUTA_BD)
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Resultados")
    perfil = cursor.fetchone()
    conexion.close()
    
    if perfil:
        for resultado in perfil:
            print(resultado)
    else:
        print(f"No se encontró ningún resultado.")
        return None


#Obtener los 3 campos de perfiles que son usados para insertar en resultados.
def obtener_perfil_por_id(id_perfil):
    conn = sqlite3.connect(RUTA_BD)
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT id, nombrePerfil, puestoTrabajo
        FROM Perfiles
        WHERE id = ?
    ''', (id_perfil,))
    
    fila = cursor.fetchone()
    conn.close()
    
    if fila:
        return {
            "id": fila[0],
            "nombrePerfil": fila[1],
            "puestoTrabajo": fila[2]
        }
    else:
        return None

#Metodos necesarios para insertar en la tabla de resultados
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


    




