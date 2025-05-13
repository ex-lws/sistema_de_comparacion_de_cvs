# Mediante esta clase se conecta a la base de datos postgreSQL 16.9
# Utilizamos PostgreSQL 16.9 y psycopg 3.1.18. Además de pgAdemin. 

# Se importan las librerías necesarias
import psycopg
from psycopg import OperationalError

def conectarBD():
    try:
        conn = psycopg.connect(
            # Credenciales de la conexion para la base de datos.
            # Modificar según sea necesario.
            dbname="PerfilesDBv1.0",
            user="postgres",
            password="admin",
            host="localhost"
        )
        print("¡Conexión exitosa!")
        return conn
    except OperationalError as e:
        print(f"Error al conectar: {e}")
        return None

# Ejemplo de uso
conexion = conectarBD()
if conexion:
    conexion.close()
