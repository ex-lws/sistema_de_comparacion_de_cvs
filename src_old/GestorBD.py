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

def borrarBD():
    import sqlite3
    # Eliminar la base de datos si existe
    conexion = sqlite3.connect(RUTA_BD)
    conexion.execute("PRAGMA foreign_keys = ON")  # Activa llaves foráneas
    cursor = conexion.cursor()
    # Ejecutar el comando para eliminar las tablas por separado
    cursor.execute('DROP TABLE IF EXISTS Resultados;')
    cursor.execute('DROP TABLE IF EXISTS Perfiles;')
    conexion.commit()
    conexion.close()

def crearTabla():
    # Crear un cursor para ejecutar comandos SQL
    conexion = sqlite3.connect(RUTA_BD)
    conexion.execute("PRAGMA foreign_keys = ON")  # Activa llaves foráneas
    cursor = conexion.cursor()
    # Crear la tabla de perfiles si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Perfiles (
            id_perfil INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_perfil TEXT NOT NULL,
            puesto_deseado TEXT,
            area_funcional TEXT,
            escolaridad TEXT,
            sueldo_mensual_minimo DOUBLE,
            sueldo_mensual_maximo DOUBLE,
            sector TEXT,
            ubicacion TEXT,
            carrera TEXT,
            edad INTEGER,
            informacion_adicional TEXT,
            herramientas_dominadas TEXT,
            habilidades_tecnicas TEXT,
            habilidades_blandas TEXT,
            logros_destacados TEXT,
            certificaciones TEXT,
            disponibilidad TEXT,
            idioma TEXT,
            nivel_idioma TEXT,
            anos_experiencia INTEGER,
            titulacion_requerida TEXT
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
            id_resultado INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_candidato TEXT NOT NULL,
            porcentaje_similitud DOUBLE,
            puesto_deseado TEXT,
            resumen TEXT,
            pdf_curriculum BLOB,
            nombre_perfil TEXT,
            id_perfil INTEGER,
            FOREIGN KEY (id_perfil) REFERENCES Perfiles(id_perfil)
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
    import sqlite3
    conexion = sqlite3.connect(RUTA_BD)
    cursor = conexion.cursor()
    cursor.execute('''
        INSERT INTO Perfiles (
            nombre_perfil,
            puesto_deseado,
            area_funcional,
            escolaridad,
            sueldo_mensual_minimo,
            sueldo_mensual_maximo,
            sector,
            ubicacion,
            carrera,
            edad,
            informacion_adicional,
            herramientas_dominadas,
            habilidades_tecnicas,
            habilidades_blandas,
            logros_destacados,
            certificaciones,
            disponibilidad,
            idioma,
            nivel_idioma,
            anos_experiencia,
            titulacion_requerida
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', parametros)
    conexion.commit()
    conexion.close()

# Buscar antes un ID en la tabla de perfiles y luego eliminarlo.

def existe_id_perfil(id_buscar):
    """
    Verifica si el ID existe en la tabla perfiles.
    """
    conexion = sqlite3.connect(RUTA_BD)
    cursor = conexion.cursor()
    cursor.execute("SELECT 1 FROM Perfiles WHERE id_perfil = ?", (id_buscar,))
    resultado = cursor.fetchone()
    conexion.close()
    return resultado is not None


# Eliminar un perfil por medio del ID. (Requiere de recoger un ID)
def eliminarPerfil(id):
    conexion = sqlite3.connect(RUTA_BD)
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM Perfiles WHERE id_perfil = ?", (id,))
    conexion.commit()
    conexion.close()
    print(f"Perfil con ID {id} eliminado.")

# Actualizar un perfil por medio del ID. (Requiere de recoger un ID y modificar parametros)
def modificarPerfil(id_perfil, parametros):
    import sqlite3
    conexion = sqlite3.connect(RUTA_BD)
    cursor = conexion.cursor()
    cursor.execute('''
        UPDATE Perfiles SET
            nombre_perfil = ?,
            puesto_deseado = ?,
            area_funcional = ?,
            escolaridad = ?,
            sueldo_mensual_minimo = ?,
            sueldo_mensual_maximo = ?,
            sector = ?,
            ubicacion = ?,
            carrera = ?,
            edad = ?,
            informacion_adicional = ?,
            herramientas_dominadas = ?,
            habilidades_tecnicas = ?,
            habilidades_blandas = ?,
            logros_destacados = ?,
            certificaciones = ?,
            disponibilidad = ?,
            idioma = ?,
            nivel_idioma = ?,
            anos_experiencia = ?,
            titulacion_requerida = ?
        WHERE id_perfil = ?
    ''', (*parametros, id_perfil))
    conexion.commit()
    conexion.close()
    print(f"Perfil con ID {id_perfil} modificado.")

# Seleccionar un perfil y guardarlo en una variable por medio de un select from id (Requiere de recabar el ID)
def obtener_perfil_por_id(id):
    conexion = sqlite3.connect(RUTA_BD)
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Perfiles WHERE id_perfil = ?", (id,))
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
def obtener_perfil_por_id_para_insertar_en_resultados(id_perfil):
    conn = sqlite3.connect(RUTA_BD)
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT id_perfil, nombre_perfil, puesto_deseado
        FROM Perfiles
        WHERE id = ?
    ''', (id_perfil,))
    
    fila = cursor.fetchone()
    conn.close()
    
    if fila:
        return {
            "id_perfil": fila[0],
            "nombre_perfil": fila[1],
            "puesto_deseado": fila[2]
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
                nombre_candidato, porcentaje_similitud, puesto_deseado, resumen, pdf_curriculum, nombre_perfil, id_perfil
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            nombre_candidato,
            porcentaje_similitud,
            perfil["puesto_deseado"],
            resumen,
            pdf_bytes,
            perfil["nombre_perfil"],
            perfil["id_perfil"]
        ))
        conn.commit()
        conn.close()


    




