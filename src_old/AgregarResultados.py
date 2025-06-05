# EXPLICACIÓN: 
# Este código permite recoger los datos necesarios para dar de alta un resultado.
# Las variables se guardan en Python para después ser insertadas con otro método en la BD (Resultados).

# VERSIÓN:
# Versión 1.5 del código. 5/06/2025.

# Importar las librerías necesarias

# Campos que requiere la talba de resultados.

# idResultado
# nombreCandidato
# porcentajeSimilitud
# puestoTrabajo -- Proviene de perfiles BD
# numeroContacto
# correoContacto
# resumen
# pdfCurriculum
# nombrePerfil -- Proviene de perfiles BD
# idPerfil -- Proviene de perfiles BD

def recogerDatosResultados():
    # idResulato es un campo automático generable.
    nombreCanidado = ""
    porcentajeSimilutd = ""
    puestoTrabajo = ""
    numeroContacto = ""
    correoContacto = ""
    resumen = ""
    pdfCurriculum = ""
    nombrePerfil = ""
    idPerfil = ""

