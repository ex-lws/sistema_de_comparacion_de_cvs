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
from pathlib import Path

# Ruta de la base de datos en el proyecto.
RUTA_BD = Path('BD/Perfiles.bd')

