# EXPLICACIÓN: 
# Este código permite realizar las diferentes acciones CRUD del sistema.

# VERSIÓN:
# Versión 2.1 del código. 25/06/2025.

# Importar las librerías necesarias
import sqlite3
from pathlib import Path
import os
from src_old.GenerarResumen import *

# Ruta de la base de datos en el proyecto, es una variable global.
RUTA_BD = Path('BD/Perfiles.bd')

# Crear la base de datos.
def crearBD():
    
    RUTA_BD.parent.mkdir(exist_ok=True)
    conexion = sqlite3.connect(RUTA_BD)
    conexion.close()

# Borrar la base de datos.
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

def borrarTablaResultados():

    conexion = sqlite3.connect(RUTA_BD)
    conexion.execute("PRAGMA foreign_keys = ON") 
    cursor = conexion.cursor()
    cursor.execute('''
        DROP TABLE IF EXISTS Resultados;
    ''')
    conexion.commit()
    conexion.close()

def borrarTablaPerfiles():

    conexion = sqlite3.connect(RUTA_BD)
    conexion.execute("PRAGMA foreign_keys = ON") 
    cursor = conexion.cursor()
    cursor.execute('''
        DROP TABLE IF EXISTS Perfiles;
    ''')
    conexion.commit()
    conexion.close()

# Crear la tabla de los perfiles.
def crearTabla():

    conexion = sqlite3.connect(RUTA_BD)
    conexion.execute("PRAGMA foreign_keys = ON") 
    cursor = conexion.cursor()
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
    conexion.commit()
    conexion.close()

# Crear la tabla de resultados.
def crearTablaResultados():
    
    conexion = sqlite3.connect(RUTA_BD)
    conexion.execute("PRAGMA foreign_keys = ON")
    cursor = conexion.cursor()
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
    conexion.commit()
    conexion.close()

# A partir de aquí inician las operaciones CRUD del sistema.

# Ver todos los perfiles
def verPerfiles():
    conexion = sqlite3.connect(RUTA_BD)
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Perfiles")
    perfiles = cursor.fetchall()
    print ("Perfiles registrados:")
    for perfil in perfiles:
        print(perfil)
    conexion.close()

# Insertar perfiles (Requiere de previamente recoger los datos a insertar en forma de una tupla)
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

# Buscar un perfil por medio del ID. (Requiere de un numero entero, en este caso el ID proporcionado).
def existe_id_perfil(id_para_buscar):
    """
    Verifica si el ID existe en la tabla perfiles.
    """
    conexion = sqlite3.connect(RUTA_BD)
    cursor = conexion.cursor()
    cursor.execute("SELECT 1 FROM Perfiles WHERE id_perfil = ?", (id_para_buscar,))
    resultado = cursor.fetchone()
    conexion.close()
    return resultado is not None


# Eliminar un perfil por medio del ID. (Requiere de recoger un ID en forma de numero entero).
def eliminarPerfil(id_para_eliminar):
    conexion = sqlite3.connect(RUTA_BD)
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM Perfiles WHERE id_perfil = ?", (id_para_eliminar,))
    conexion.commit()
    conexion.close()
    print(f"Perfil con ID {id} eliminado.")

# Actualizar un perfil por medio del ID y por medio de parametros nuevos. (Requiere de recoger un ID y modificar parametros)
def modificarPerfil(id_perfil_para_actualizar, parametros_nuevos):
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
    ''', (*parametros_nuevos, id_perfil_para_actualizar))
    conexion.commit()
    conexion.close()
    print(f"Perfil con ID {id_perfil_para_actualizar} modificado.")

# Obtener un perfil por medio de un ID (requerido) y convertirlo de una variable.
def obtener_perfil_por_id(id_para_obtener_perfil):
    conexion = sqlite3.connect(RUTA_BD)
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Perfiles WHERE id_perfil = ?", (id_para_obtener_perfil,))
    perfil = cursor.fetchone()
    conexion.close()
    
    if perfil:
        return perfil
    else:
        print(f"No se encontró un perfil con ID {id_para_obtener_perfil}.")
        return None
    
# Mostrar los registros de la tabla Resultados ordenados por porcentaje de similitud descendente.
def verResultadosTabla():
    conexion = sqlite3.connect(RUTA_BD)
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Resultados ORDER BY porcentaje_similitud DESC")
    resultados = cursor.fetchall()
    conexion.close()
    
    if resultados:
        for resultado in resultados:
            print(resultado)
    else:
        print(f"No se encontró ningún resultado.")
        return None

# Inicia lógica para poder insertar en la tabla Resultados.
# Requiere de recabar datos tanto de los archivos PDF como de los perfiles.

#Obtener los 3 campos de la tabla Perfiles que son usados para insertar en resultados.
def obtener_perfil_por_id_para_insertar_en_resultados(id_perfil):
    conn = sqlite3.connect(RUTA_BD)
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT id_perfil, nombre_perfil, puesto_deseado
        FROM Perfiles
        WHERE id_perfil = ?
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

# Función para extraer el nombre del candidato desde el nombre del archivo.
# Este es un valor necesario para insertar en la tabla Resultados.

'''
def extraer_nombre_candidato(nombre_archivo):
    nombre_base = os.path.basename(nombre_archivo)
    nombre_sin_extension = os.path.splitext(nombre_base)[0]
    partes = nombre_sin_extension.split('_')

    if len(partes) >= 3 and partes[0].strip().upper() == "CV":
        return ' '.join(partes[1:-1]).strip()
    else:
        return "Desconocido"
'''

def extraer_nombre_candidato(nombre_archivo):
    # Asume que el nombre es algo como: "CV_JUAN PÉREZ_MARKETING.pdf"
    base = os.path.basename(nombre_archivo)
    nombre = os.path.splitext(base)[0]
    nombre = nombre.replace("CV", "").replace("_", " ").strip()
    return nombre

# Insertar valores extraídos en la tabla Resultados.
# Requiere de: Diccionario con los resultados tras la comparación, ruta de los cvs definitivos, perfil y la ruta de la base de datos.
# Por otro lado, se tienen metodos embebidos que extraen texto del PDF para crear un resumen del mismo (Dato requerido para esta tabla de Resultados).
def insertar_resultados_comparacion(resultadosComparacion, ruta_definitiva, datos_perfil,id_perfil):
    for nombre_archivo, porcentaje_similitud in resultadosComparacion.items():
        ruta_pdf = os.path.join(ruta_definitiva, os.path.basename(nombre_archivo))
        # Preparación de los datos para insertar en la tabla Resultados.
        #id_del_perfil = obtener_perfil_por_id_para_insertar_en_resultados(id_perfil_seleccionado)
        nombre_candidato = extraer_nombre_candidato(nombre_archivo)
        resumen = procesar_cv(ruta_pdf)
        datos_perfil = obtener_perfil_por_id_para_insertar_en_resultados(id_perfil)

        with open(ruta_pdf, "rb") as f:
            pdf_bytes = f.read()

        conn = sqlite3.connect(RUTA_BD)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Resultados (
                nombre_candidato, porcentaje_similitud, puesto_deseado, resumen, pdf_curriculum, nombre_perfil, id_perfil
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            nombre_candidato,
            porcentaje_similitud,
            datos_perfil["puesto_deseado"],
            resumen,
            pdf_bytes,
            datos_perfil["nombre_perfil"],
            id_perfil
        ))
        conn.commit()
        conn.close()
