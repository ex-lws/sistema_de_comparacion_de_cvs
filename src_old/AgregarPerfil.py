# EXPLICACIÓN: 
# Este código permite recoger los datos necesarios para dar de alta un perfil.
# Los datos se guardan en variables tipo String de Python.

# VERSIÓN:
# Versión 1.5 del código. 05/06/2025.

# Importar las librerías necesarias

from src_old.GestorBD import *

def recabarDatos():
    # Recabar datos
    # Variables y solicitudes por medio de consola.

    # Nombre del perfil

    nombrePerfil = input("Escriba el nombre del perfil")

    # Puesto deseado

    puestoDeseado = input("Escriba el puesto deseado")

    # Area funcional

    areaFuncional = input("Escriba el área funcional")

    # Escolaridad

    escolaridad = input("Escriba la escolaridad")

    # Sueldo mensual minimo

    sueldoMinimo = input("Escriba el sueldo mensual mínimo")

    # Sueldo mensual maximo

    sueldoMaximo = input("Escriba el sueldo mensual máximo")

    # Sector

    sector = input("Escriba el sector")

    # Ubicación

    ubicacion = input("Escriba la ubicación")

    # Carrera

    carrera = input("Escriba la carrera")

    # Edad

    edad = input("Escriba la edad")

    # Información adicional

    informacionAdicional = input("Escriba la información adicional")

    # Herramientas dominadas

    herramientasDominadas = input("Escriba las herramientas dominadas")

    # Habilidades tecnicas

    habilidadesTecnicas = input("Escriba las habilidades técnicas")

    # Habilidades blandas

    habilidadesBlandas = input("Escriba las habilidades blandas")

    # Logros destacados

    logrosDestacados = input("Escriba los logros destacados")

    # Certificaciones

    certificaciones = input("Escriba las certificaciones")

    # Disponibilidad

    disponibilidad = input("Escriba la disponibilidad")

    # Idioma

    idioma = input("Escriba el idioma")

    # Nivel de idioma

    nivelIdioma = input("Escriba el nivel del idioma")

    # Años de experiencia

    anosExperiencia = input("Escriba los años de experiencia")

    # Titulacion requerida

    titulacionRequerida = input("Escriba la titulación requerida")

    # Retornar en una tupla

    return (nombrePerfil, puestoDeseado, areaFuncional, escolaridad, sueldoMinimo, sueldoMaximo,
            sector, ubicacion, carrera, edad, informacionAdicional, herramientasDominadas,
            habilidadesTecnicas, habilidadesBlandas, logrosDestacados, certificaciones,
            disponibilidad, idioma, nivelIdioma, anosExperiencia, titulacionRequerida)




