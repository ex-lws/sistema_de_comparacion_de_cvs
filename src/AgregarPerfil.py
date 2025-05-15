#Este codigo permite agregar un nuevo perfil al sistema

#Versión 1.0 del código. 15/05/2025

def recabarDatos():
    # Variables y solicitudes por medio de consola.

    # Tipo de contratación
    seleccion_1 = input("Seleccione el tipo de contratacion: \
                        \n1.- Tiempo indeterminado, 2.- Becario, 3.- Por proyecto.")
    
    if seleccion_1 == "1":
        tipoContratacion = "Tiempo Indeterminado"  
    elif seleccion_1 == "2":
        tipoContratacion = "Becario"
    elif seleccion_1 == "3":
        tipoContratacion = "Por Proyecto"   
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
        return None
    
    # Horario de trabajo
    seleccion_2 = input("Ingrese el horario de trabajo: \
                        \n1.- Tiempo completo, 2.- Medio tiempo.")
    
    if seleccion_2 == "1":
        horarioTrabajo = "Tiempo Completo"
    elif seleccion_2 == "2":
        horarioTrabajo = "Medio Tiempo"
    else:
        print("Opcion no valida. Por favor, seleccione una opción válida.")
        return None
    
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
        return None

    # Salario minmo 
    seleccion_4 = float(input("Ingrese el salario minimo:"))
    if seleccion_4 > 0:
        salarioMinimo = seleccion_4
    else:
        print("Opcion no valida. Por favor, seleccione una opción válida.")
        return None
    
    # Salario maximo
    seleccion_5 = float(input("Ingrese el salario maximo:"))
    if seleccion_5 > 0 and seleccion_5 <= 10000000:
        salarioMaximo = seleccion_5
    else:
        print("Opcion no valida. Por favor, seleccione una opción válida.")
        return None
    
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
        return None
    
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
        areaTrabajo = "Administracion/Oficina"
    elif seleccion_7 == "2":        
        areaTrabajo = "Almacen/Logistica/Transporte"    
    elif seleccion_7 == "3":    
        areaTrabajo = "Atencion a clientes"
    elif seleccion_7 == "4":
        areaTrabajo = "Call center/Telemercado"
    elif seleccion_7 == "5":
        areaTrabajo = "Compras/Comercio exterior"
    elif seleccion_7 == "6":
        areaTrabajo = "Construccion/Obra"  
    elif seleccion_7 == "7":
        areaTrabajo = "Contabilidad/Finanzas"
    elif seleccion_7 == "8":
        areaTrabajo = "Direccion/Gerencia"
    elif seleccion_7 == "9":
        areaTrabajo = "Diseno/Artes graficas"
    elif seleccion_7 == "10":
        areaTrabajo = "Docencia"
    elif seleccion_7 == "11":
        areaTrabajo = "Hosteleria/Turismo"
    elif seleccion_7 == "12":
        areaTrabajo = "Informatica/Telecomunicaciones"
    elif seleccion_7 == "13":
        areaTrabajo = "Ingenieria"
    elif seleccion_7 == "14":
        areaTrabajo = "Investigacion y calidad" 
    elif seleccion_7 == "15":
        areaTrabajo = "Legal/Asesoria"
    elif seleccion_7 == "16":
        areaTrabajo = "Mantenimiento y reparaciones tecnicas"
    elif seleccion_7 == "17":
        areaTrabajo = "Medicina/Salud"
    elif seleccion_7 == "18":
        areaTrabajo = "Mercadotecnia/Publicidad/Comunicacion"
    elif seleccion_7 == "19":
        areaTrabajo = "Operarios/Produccion/Manufactura"
    elif seleccion_7 == "20":
        areaTrabajo = "Recursos humanos"
    elif seleccion_7 == "21":
        areaTrabajo = "Servicios generales"
    elif seleccion_7 == "22":
        areaTrabajo = "Aseo y seguridad"
    elif seleccion_7 == "23":
        areaTrabajo = "Otros"
    else:
        print("Opcion no valida. Por favor, seleccione una opción válida.")
        return None      
        
    # Puesto 
    puestoTrabajo = input("Ingrese el puesto de trabajo")
    if puestoTrabajo == "":
        print("Opcion no valida. Por favor, seleccione una opción válida.")
        return None
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
        return None

    # Idioma (Solo idiomas comunes aparte del español)
    seleccion_9 = input("Ingresa el idioma: \n1.- Ingles, 2.- Frances, 3.- Portugues, 4.- Italiano, 5.- Aleman")
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
    else:
        print("Opcion no valida. Por favor, seleccione una opción válida.")
        return None
    
    # Nivel de idioma
    seleccion_10 = input("Ingrese el nivel de idioma: \
                         \n1.- Basico, 2.- Intermedio, 3.- Avanzado.")
    if seleccion_10 == "1":
        nivelIdioma = "Basico"
    elif seleccion_10 == "2":
        nivelIdioma = "Intermedio"
    elif seleccion_10 == "3":
        nivelIdioma = "Avanzado"
    else:
        print("Opcion no valida. Por favor, seleccione una opción válida.")
        return None
    
    # Licencia de conducir
    seleccion_11 = input("Ingrese la licencia de conducir \
                         \n1.- Si, 2.- No.")
    if seleccion_11 == "1":
        licenciaConducir = "Si"
    elif seleccion_11 == "2":
        licenciaConducir = "No"
    else:
        print("Opcion no valida. Por favor, seleccione una opción válida.")
        return None
    
    # Años de experiencia
    seleccion_12 = int(input("Ingrese los años de experiencia:"))
    if seleccion_12 >= 0 and seleccion_12 <= 80:
        anosExperiencia = seleccion_12
    else:
        print("Opcion no valida. Por favor, seleccione una opción válida.")
        return None
    
    # Final del registro
    print("Los datos han sido registrados correctamente")
    print ("Tipo de contratacion: ", tipoContratacion)
    print ("Horario de trabajo: ", horarioTrabajo)      
    print ("Modalidad de trabajo: ", modalidadTrabajo)
    print ("Salario minimo: ", salarioMinimo)
    print ("Salario maximo: ", salarioMaximo)
    print ("Escolaridad: ", escolaridad)
    print ("Area de trabajo: ", areaTrabajo)
    print ("Puesto de trabajo: ", puestoTrabajo)
    print ("Ubicacion: ", ubicacion)
    print ("Idioma: ", idioma)
    print ("Nivel de idioma: ", nivelIdioma)
    print ("Licencia de conducir: ", licenciaConducir)
    print ("Años de experiencia: ", anosExperiencia)

recabarDatos()