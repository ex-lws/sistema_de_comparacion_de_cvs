# Mediante esta clase se hacen los diversos metodos para interactuar con la base de datos.
# Crear la base de datos.
# Crear la tabla.
# Operaciones CRUD.

# Versión 1.0 del código. 21/05/2025

# Librerías necesarias
import sqlite3
from pathlib import Path


RUTA_BD = Path('BD/Perfiles.bd')

def crearBD():
    # Crear carpeta si no existe
    RUTA_BD.parent.mkdir(exist_ok=True)
    # Conectar a la base de datos (se crea si no existe)
    conexion = sqlite3.connect(RUTA_BD)
    print("Base de datos creada o ya existe.")
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
    print ("Tabla 'Perfiles' creada o ya existe.")
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
        CREATE TABLE IF NOT EXISTS CurriculumsDefinitivos (
            idOperacion INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            correo TEXT NOT NULL,
            telefono TEXT NOT NULL,
            idPerfil INTEGER NOT NULL,
            FOREIGN KEY (idPerfil) REFERENCES Perfiles(id)
        )
    ''')
    print ("Tabla 'CurriculumsDefinitivos' creada o ya existe.")
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

def eliminarPerfil(id):
    conexion = sqlite3.connect(RUTA_BD)
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM Perfiles WHERE id = ?", (id,))
    conexion.commit()
    conexion.close()
    print(f"Perfil con ID {id} eliminado.")

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



    




