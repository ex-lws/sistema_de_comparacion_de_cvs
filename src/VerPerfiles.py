# Este código permite ver los perfiles registrados en la base de datos. 

# Versión 1.0 del código. 13/05/2025

# Importar las librerías necesarias

import psycopg
from psycopg import OperationalError
from ConectarBD import conectarBD # Método para conectarnos a la base de datos

def verPerfiles ():

    # Conectamos a la base de datos por medio de herencia.

    conectar = conectarBD()
    if not conectar:
        print("No se pudo conectar a la base de datos")
        return None
    
    with conectar.cursor() as cursor:
        try:
            # Ejecutamos la consulta para ver los perfiles registrados en la base de datos.
            cursor.execute("SELECT * FROM perfiles")
            # Obtenemos todos los resultados de la consulta.
            resultados = cursor.fetchall()
            # Imprimimos los resultados.
            for resultado in resultados:
                print(resultado)
        except OperationalError as e:
            print(f"Error al ejecutar la consulta: {e}")
        finally:
            conectar.close()

verPerfiles()
    

