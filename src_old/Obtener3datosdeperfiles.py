# EXPLICACIÓN: 
# Este código permite subir los cirruculums aún sin limpiar a la carpeta de CVS Teamporales.

# VERSIÓN:
# Versión 1.0 del código. 13/05/2025.

# Importar las librerías necesarias

import sqlite3
from pathlib import Path

RUTA_BD = Path('BD/Perfiles.bd')

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

abajo = None

# Ahora las variables id_perfil, nombre_perfil y puesto_trabajo contienen los datos o None si no se encontró el perfil

