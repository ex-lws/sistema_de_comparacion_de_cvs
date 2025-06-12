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

    # Tipo de contratación
    seleccion_1 = input("Seleccione el tipo de contratacion: \
                        \n1.- Tiempo indeterminado, 2.- Becario, 3.- Por proyecto, 4.- No aplica.")

    if seleccion_1 == "1":
        tipoContratacion = "Tiempo Indeterminado"  
    elif seleccion_1 == "2":
        tipoContratacion = "Becario"
    elif seleccion_1 == "3":
        tipoContratacion = "Por Proyecto"
    elif seleccion_1 == "4":
        tipoContratacion = "No aplica"   
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
        

    # Horario de trabajo
    seleccion_2 = input("Ingrese el horario de trabajo: \
                        \n1.- Tiempo completo, 2.- Medio tiempo, 3.- Por honorarios.")

    if seleccion_2 == "1":
        horarioTrabajo = "Tiempo Completo"
    elif seleccion_2 == "2":
        horarioTrabajo = "Medio Tiempo"
    elif seleccion_2 == "3":
        horarioTrabajo = "Por honorarios"
    else:
        print("Opcion no valida. Por favor, seleccione una opción válida.")
        

    #Modalidad de trabajo
    seleccion_3 = input("Ingrese la modalidad de trabajo: \
                        \n1.- Presencial, 2.- Hibrida, 3.-Remoto.")

    if seleccion_3 == "1":
        modalidadTrabajo = "Presencial"
    elif seleccion_3 == "2":
        modalidadTrabajo = "Hibrida"
    elif seleccion_3 == "3":
        modalidadTrabajo = "Remoto"
    else:
        print("Opcion no valida. Por favor, seleccione una opción válida.")
        

    # Salario minmo 
    seleccion_4 = float(input("Ingrese el salario minimo:"))
    if seleccion_4 > 0:
        sueldoMensualMinimo = seleccion_4
    else:
        print("Opcion no valida. Por favor, seleccione una opción válida.")
        

    # Salario maximo
    seleccion_5 = float(input("Ingrese el salario maximo:"))
    if seleccion_5 > 0 and seleccion_5 <= 10000000:
        sueldoMensualMaximo = seleccion_5
    else:
        print("Opcion no valida. Por favor, seleccione una opción válida.")
        

    # Escolaridad
    seleccion_6 = input("Ingrese la escolaridad: \
                        \n1.- Educacion basica, 2.- Educacion medio superior, 3.- Educacion superior.")
    if seleccion_6 == "1":
        escolaridad = "Educacion Basica"
    elif seleccion_6 == "2":
        escolaridad = "Educacion Medio Superior"
    elif seleccion_6 == "3":
        escolaridad = "Educacion Superior"
    else:
        print("Opcion no valida. Por favor, seleccione una opción válida.")
        

    # Area de trabajo
    seleccion_7 = input("Ingrese el area de trabajo: \
                        \n1.- Administracion/Oficina, 2.- Almacen/Logistica/Transporte, 3.- Atencion a clientes " \
                        "\n4.- Call center/Telemercado, 5.- Compras/Comercio exterior, 6.- Construccion/Obra, " \
                        "\n7.- Contabilidad/Finanzas, 8.- Direccion/Gerencia, 9.- Diseño/Artes graficas, " \
                        "\n10.- Docencia, 11.- Hosteleria/Turismo, 12.- Informatica/Telecomunicaciones, " \
                        "\n13.- Ingenieria, 14.- Investigacion y calidad, 15.- Legal/Asesoria, " \
                        "\n16.- Mantenimiento y reparaciones tecnicas, 17.- Medicina/Salud, 18.- Mercadotecnia/Publicidad/Comunicacion, " \
                        "\n19.- Operarios/Produccion/Manufactura, 20.- Recursos humanos, 21.- Servicios generales, " \
                        "\n22.- Aseo y seguridad, 23.- Otros.")

    if seleccion_7 == "1":
        area = "Administracion/Oficina"
    elif seleccion_7 == "2":        
        area = "Almacen/Logistica/Transporte"    
    elif seleccion_7 == "3":    
        area = "Atencion a clientes"
    elif seleccion_7 == "4":
        area = "Call center/Telemercado"
    elif seleccion_7 == "5":
        area = "Compras/Comercio exterior"
    elif seleccion_7 == "6":
        area = "Construccion/Obra"  
    elif seleccion_7 == "7":
        area = "Contabilidad/Finanzas"
    elif seleccion_7 == "8":
        area = "Direccion/Gerencia"
    elif seleccion_7 == "9":
        area = "Diseno/Artes graficas"
    elif seleccion_7 == "10":
        area = "Docencia"
    elif seleccion_7 == "11":
        area = "Hosteleria/Turismo"
    elif seleccion_7 == "12":
        area = "Informatica/Telecomunicaciones"
    elif seleccion_7 == "13":
        area = "Ingenieria"
    elif seleccion_7 == "14":
        area = "Investigacion y calidad" 
    elif seleccion_7 == "15":
        area = "Legal/Asesoria"
    elif seleccion_7 == "16":
        area = "Mantenimiento y reparaciones tecnicas"
    elif seleccion_7 == "17":
        area = "Medicina/Salud"
    elif seleccion_7 == "18":
        area = "Mercadotecnia/Publicidad/Comunicacion"
    elif seleccion_7 == "19":
        area = "Operarios/Produccion/Manufactura"
    elif seleccion_7 == "20":
        area = "Recursos humanos"
    elif seleccion_7 == "21":
        area = "Servicios generales"
    elif seleccion_7 == "22":
        area = "Aseo y seguridad"
    elif seleccion_7 == "23":
        area = "Otros"
    else:
        print("Opcion no valida. Por favor, seleccione una opción válida.")
            
        
    # Puesto 
    puestoTrabajo = input("Ingrese el puesto de trabajo")
    if puestoTrabajo == "":
        print("Opcion no valida. Por favor, seleccione una opción válida.")
        
    else:
        puestoTrabajo = puestoTrabajo

    # Ubicación
    seleccion_8 = input("Ingrese la ubicacion: \
                        \n1.- Aguascalientes, 2.- Baja California, 3.- Baja California Sur \n" \
                        "4.- Campeche, 5.- Chiapas, 6.- Chihuahua\n," \
                        "7.- Coahuila, 8.- Colima, 9.-Hidalgo\n"\
                        "10.- Jalisco, 11.- Durango, 12.- Michoacan\n" \
                        "13.- Morelos, 14.- Nayarit, 15.- Nuevo Leon\n" \
                        "16.- Oaxaca, 17.- Puebla, 18.- Queretaro\n" \
                        "19.- Quintana Roo, 20.- San Luis Potosi\n" \
                        "21.- Sinaloa, 22.- Sonora, 23.- Tabasco\n" \
                        "24.- Tamaulipas, 25.- Tlaxcala, 26.- Veracruz\n" \
                        "27.- Yucatan, 28.- Zacatecas, 29.- Ciudad de Mexico\n" \
                        "30.- Estado de Mexico, 31.- Guerrero, 32.- Guanajuato.\n")

    if seleccion_8 == "1":
        ubicacion = "Aguascalientes"
    elif seleccion_8 == "2":    
        ubicacion = "Baja California"
    elif seleccion_8 == "3":
        ubicacion = "Baja California Sur"
    elif seleccion_8 == "4":
        ubicacion = "Campeche"
    elif seleccion_8 == "5":
        ubicacion = "Chiapas"
    elif seleccion_8 == "6":
        ubicacion = "Chihuahua"
    elif seleccion_8 == "7":
        ubicacion = "Coahuila"
    elif seleccion_8 == "8":
        ubicacion = "Colima"
    elif seleccion_8 == "9":
        ubicacion = "Hidalgo"
    elif seleccion_8 == "10":
        ubicacion = "Jalisco"
    elif seleccion_8 == "11":
        ubicacion = "Durango"
    elif seleccion_8 == "12":
        ubicacion = "Michoacan"
    elif seleccion_8 == "13":
        ubicacion = "Morelos"
    elif seleccion_8 == "14":
        ubicacion = "Nayarit"
    elif seleccion_8 == "15":
        ubicacion = "Nuevo Leon"
    elif seleccion_8 == "16":
        ubicacion = "Oaxaca"
    elif seleccion_8 == "17":
        ubicacion = "Puebla"
    elif seleccion_8 == "18":
        ubicacion = "Queretaro"
    elif seleccion_8 == "19":
        ubicacion = "Quintana Roo"
    elif seleccion_8 == "20":
        ubicacion = "San Luis Potosi"
    elif seleccion_8 == "21":
        ubicacion = "Sinaloa"
    elif seleccion_8 == "22":
        ubicacion = "Sonora"
    elif seleccion_8 == "23":
        ubicacion = "Tabasco"
    elif seleccion_8 == "24":
        ubicacion = "Tamaulipas"
    elif seleccion_8 == "25":
        ubicacion = "Tlaxcala"
    elif seleccion_8 == "26":
        ubicacion = "Veracruz"
    elif seleccion_8 == "27":
        ubicacion = "Yucatan"
    elif seleccion_8 == "28":
        ubicacion = "Zacatecas"
    elif seleccion_8 == "29":   
        ubicacion = "Ciudad de Mexico"
    elif seleccion_8 == "30":
        ubicacion = "Estado de Mexico"
    elif seleccion_8 == "31":
        ubicacion = "Guerrero"
    elif seleccion_8 == "32":
        ubicacion = "Guanajuato"
    else:   
        print("Opcion no valida. Por favor, seleccione una opción válida.")
        

    # Idioma (Solo idiomas comunes aparte del español)
    seleccion_9 = input("Ingresa el idioma: \n1.- Ingles, 2.- Frances, 3.- Portugues, 4.- Italiano, 5.- Aleman, 6.- No aplica.")
    if seleccion_9 == "1":
        idioma = "Ingles"
    elif seleccion_9 == "2":
        idioma = "Frances"
    elif seleccion_9 == "3":
        idioma = "Portugues"
    elif seleccion_9 == "4":
        idioma = "Italiano"
    elif seleccion_9 == "5":
        idioma = "Aleman"
    elif seleccion_9 == "6":
        idioma = "No aplica"
    else:
        print("Opcion no valida. Por favor, seleccione una opción válida.")
        

    # Nivel de idioma
    seleccion_10 = input("Ingrese el nivel de idioma: \
                            \n1.- Basico, 2.- Intermedio, 3.- Avanzado, 4.- No aplica.")
    if seleccion_10 == "1":
        nivelIdioma = "Basico"
    elif seleccion_10 == "2":
        nivelIdioma = "Intermedio"
    elif seleccion_10 == "3":
        nivelIdioma = "Avanzado"
    elif seleccion_10 == "4":
        nivelIdioma = "No aplica"
    else:
        print("Opcion no valida. Por favor, seleccione una opción válida.")
        

    # Licencia de conducir
    seleccion_11 = input("Ingrese la licencia de conducir \
                            \n1.- Si, 2.- No.")
    if seleccion_11 == "1":
        licenciaConducir = "Si"
    elif seleccion_11 == "2":
        licenciaConducir = "No"
    else:
        print("Opcion no valida. Por favor, seleccione una opción válida.")
        

    # Años de experiencia
    seleccion_12 = int(input("Ingrese los años de experiencia:"))
    if seleccion_12 >= 0 and seleccion_12 <= 80:
        anosExperiencia = seleccion_12
    else:
        print("Opcion no valida. Por favor, seleccione una opción válida.")
        

    # Final del registro
    print("Los datos han sido registrados correctamente")
    print ("Nombre del perfil:", nombrePerfil)
    print ("Tipo de contratacion: ", tipoContratacion)
    print ("Horario de trabajo: ", horarioTrabajo)      
    print ("Modalidad de trabajo: ", modalidadTrabajo)
    print ("Salario minimo: ", sueldoMensualMinimo)
    print ("Salario maximo: ", sueldoMensualMaximo)
    print ("Escolaridad: ", escolaridad)
    print ("Area de trabajo: ", area)
    print ("Puesto de trabajo: ", puestoTrabajo)
    print ("Ubicacion: ", ubicacion)
    print ("Idioma: ", idioma)
    print ("Nivel de idioma: ", nivelIdioma)
    print ("Licencia de conducir: ", licenciaConducir)
    print ("Años de experiencia: ", anosExperiencia)

    # Codigo para insertar los datos en la base de datos con SQLite.
    return (nombrePerfil, tipoContratacion, horarioTrabajo, modalidadTrabajo, sueldoMensualMinimo, sueldoMensualMaximo, escolaridad, area, puestoTrabajo, ubicacion, idioma, nivelIdioma, licenciaConducir, anosExperiencia)





