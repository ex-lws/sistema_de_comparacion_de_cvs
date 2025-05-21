<?php
<?php

// Este código permite agregar un nuevo perfil al sistema
// Versión 1.1 del código. 21/05/2025
// Reconversion a PHP. 

require_once 'ConectarBD.php'; // Método para conectarnos a la base de datos

function leer($mensaje) {
    echo $mensaje . "\n";
    return trim(fgets(STDIN));
}

function insertarDatos() {
    // Tipo de contratación
    $seleccion_1 = leer("Seleccione el tipo de contratacion:\n1.- Tiempo indeterminado, 2.- Becario, 3.- Por proyecto.");
    if ($seleccion_1 == "1") {
        $tipoContratacion = "Tiempo Indeterminado";
    } elseif ($seleccion_1 == "2") {
        $tipoContratacion = "Becario";
    } elseif ($seleccion_1 == "3") {
        $tipoContratacion = "Por Proyecto";
    } else {
        echo "Opción no válida. Por favor, seleccione una opción válida.\n";
        return;
    }

    // Horario de trabajo
    $seleccion_2 = leer("Ingrese el horario de trabajo:\n1.- Tiempo completo, 2.- Medio tiempo.");
    if ($seleccion_2 == "1") {
        $horarioTrabajo = "Tiempo Completo";
    } elseif ($seleccion_2 == "2") {
        $horarioTrabajo = "Medio Tiempo";
    } else {
        echo "Opcion no valida. Por favor, seleccione una opción válida.\n";
        return;
    }

    // Modalidad de trabajo
    $seleccion_3 = leer("Ingrese la modalidad de trabajo:\n1.- Presencial, 2.- Hibrida, 3.-Remoto.");
    if ($seleccion_3 == "1") {
        $modalidadTrabajo = "Presencial";
    } elseif ($seleccion_3 == "2") {
        $modalidadTrabajo = "Hibrida";
    } elseif ($seleccion_3 == "3") {
        $modalidadTrabajo = "Remoto";
    } else {
        echo "Opcion no valida. Por favor, seleccione una opción válida.\n";
        return;
    }

    // Salario mínimo
    $seleccion_4 = floatval(leer("Ingrese el salario minimo:"));
    if ($seleccion_4 > 0) {
        $salarioMinimo = $seleccion_4;
    } else {
        echo "Opcion no valida. Por favor, seleccione una opción válida.\n";
        return;
    }

    // Salario máximo
    $seleccion_5 = floatval(leer("Ingrese el salario maximo:"));
    if ($seleccion_5 > 0 && $seleccion_5 <= 10000000) {
        $salarioMaximo = $seleccion_5;
    } else {
        echo "Opcion no valida. Por favor, seleccione una opción válida.\n";
        return;
    }

    // Escolaridad
    $seleccion_6 = leer("Ingrese la escolaridad:\n1.- Educacion basica, 2.- Educacion medio superior, 3.- Educacion superior.");
    if ($seleccion_6 == "1") {
        $escolaridad = "Educacion Basica";
    } elseif ($seleccion_6 == "2") {
        $escolaridad = "Educacion Medio Superior";
    } elseif ($seleccion_6 == "3") {
        $escolaridad = "Educacion Superior";
    } else {
        echo "Opcion no valida. Por favor, seleccione una opción válida.\n";
        return;
    }

    // Área de trabajo
    $seleccion_7 = leer("Ingrese el area de trabajo:\n1.- Administracion/Oficina, 2.- Almacen/Logistica/Transporte, 3.- Atencion a clientes\n4.- Call center/Telemercado, 5.- Compras/Comercio exterior, 6.- Construccion/Obra,\n7.- Contabilidad/Finanzas, 8.- Direccion/Gerencia, 9.- Diseño/Artes graficas,\n10.- Docencia, 11.- Hosteleria/Turismo, 12.- Informatica/Telecomunicaciones,\n13.- Ingenieria, 14.- Investigacion y calidad, 15.- Legal/Asesoria,\n16.- Mantenimiento y reparaciones tecnicas, 17.- Medicina/Salud, 18.- Mercadotecnia/Publicidad/Comunicacion,\n19.- Operarios/Produccion/Manufactura, 20.- Recursos humanos, 21.- Servicios generales,\n22.- Aseo y seguridad, 23.- Otros.");
    $areas = [
        "1" => "Administracion/Oficina", "2" => "Almacen/Logistica/Transporte", "3" => "Atencion a clientes",
        "4" => "Call center/Telemercado", "5" => "Compras/Comercio exterior", "6" => "Construccion/Obra",
        "7" => "Contabilidad/Finanzas", "8" => "Direccion/Gerencia", "9" => "Diseno/Artes graficas",
        "10" => "Docencia", "11" => "Hosteleria/Turismo", "12" => "Informatica/Telecomunicaciones",
        "13" => "Ingenieria", "14" => "Investigacion y calidad", "15" => "Legal/Asesoria",
        "16" => "Mantenimiento y reparaciones tecnicas", "17" => "Medicina/Salud", "18" => "Mercadotecnia/Publicidad/Comunicacion",
        "19" => "Operarios/Produccion/Manufactura", "20" => "Recursos humanos", "21" => "Servicios generales",
        "22" => "Aseo y seguridad", "23" => "Otros"
    ];
    if (array_key_exists($seleccion_7, $areas)) {
        $areaTrabajo = $areas[$seleccion_7];
    } else {
        echo "Opcion no valida. Por favor, seleccione una opción válida.\n";
        return;
    }

    // Puesto
    $puestoTrabajo = leer("Ingrese el puesto de trabajo:");
    if ($puestoTrabajo == "") {
        echo "Opcion no valida. Por favor, seleccione una opción válida.\n";
        return;
    }

    // Ubicación
    $seleccion_8 = leer("Ingrese la ubicacion:\n1.- Aguascalientes, 2.- Baja California, 3.- Baja California Sur\n4.- Campeche, 5.- Chiapas, 6.- Chihuahua\n7.- Coahuila, 8.- Colima, 9.-Hidalgo\n10.- Jalisco, 11.- Durango, 12.- Michoacan\n13.- Morelos, 14.- Nayarit, 15.- Nuevo Leon\n16.- Oaxaca, 17.- Puebla, 18.- Queretaro\n19.- Quintana Roo, 20.- San Luis Potosi\n21.- Sinaloa, 22.- Sonora, 23.- Tabasco\n24.- Tamaulipas, 25.- Tlaxcala, 26.- Veracruz\n27.- Yucatan, 28.- Zacatecas, 29.- Ciudad de Mexico\n30.- Estado de Mexico, 31.- Guerrero, 32.- Guanajuato.");
    $ubicaciones = [
        "1" => "Aguascalientes", "2" => "Baja California", "3" => "Baja California Sur", "4" => "Campeche",
        "5" => "Chiapas", "6" => "Chihuahua", "7" => "Coahuila", "8" => "Colima", "9" => "Hidalgo",
        "10" => "Jalisco", "11" => "Durango", "12" => "Michoacan", "13" => "Morelos", "14" => "Nayarit",
        "15" => "Nuevo Leon", "16" => "Oaxaca", "17" => "Puebla", "18" => "Queretaro", "19" => "Quintana Roo",
        "20" => "San Luis Potosi", "21" => "Sinaloa", "22" => "Sonora", "23" => "Tabasco", "24" => "Tamaulipas",
        "25" => "Tlaxcala", "26" => "Veracruz", "27" => "Yucatan", "28" => "Zacatecas", "29" => "Ciudad de Mexico",
        "30" => "Estado de Mexico", "31" => "Guerrero", "32" => "Guanajuato"
    ];
    if (array_key_exists($seleccion_8, $ubicaciones)) {
        $ubicacion = $ubicaciones[$seleccion_8];
    } else {
        echo "Opcion no valida. Por favor, seleccione una opción válida.\n";
        return;
    }

    // Idioma
    $seleccion_9 = leer("Ingresa el idioma:\n1.- Ingles, 2.- Frances, 3.- Portugues, 4.- Italiano, 5.- Aleman");
    $idiomas = ["1" => "Ingles", "2" => "Frances", "3" => "Portugues", "4" => "Italiano", "5" => "Aleman"];
    if (array_key_exists($seleccion_9, $idiomas)) {
        $idioma = $idiomas[$seleccion_9];
    } else {
        echo "Opcion no valida. Por favor, seleccione una opción válida.\n";
        return;
    }

    // Nivel de idioma
    $seleccion_10 = leer("Ingrese el nivel de idioma:\n1.- Basico, 2.- Intermedio, 3.- Avanzado.");
    $niveles = ["1" => "Basico", "2" => "Intermedio", "3" => "Avanzado"];
    if (array_key_exists($seleccion_10, $niveles)) {
        $nivelIdioma = $niveles[$seleccion_10];
    } else {
        echo "Opcion no valida. Por favor, seleccione una opción válida.\n";
        return;
    }

    // Licencia de conducir
    $seleccion_11 = leer("Ingrese la licencia de conducir\n1.- Si, 2.- No.");
    if ($seleccion_11 == "1") {
        $licenciaConducir = "Si";
    } elseif ($seleccion_11 == "2") {
        $licenciaConducir = "No";
    } else {
        echo "Opcion no valida. Por favor, seleccione una opción válida.\n";
        return;
    }

    // Años de experiencia
    $seleccion_12 = intval(leer("Ingrese los años de experiencia:"));
    if ($seleccion_12 >= 0 && $seleccion_12 <= 80) {
        $anosExperiencia = $seleccion_12;
    } else {
        echo "Opcion no valida. Por favor, seleccione una opción válida.\n";
        return;
    }

    // Mostrar datos
    echo "Los datos han sido registrados correctamente\n";
    echo "Tipo de contratacion: $tipoContratacion\n";
    echo "Horario de trabajo: $horarioTrabajo\n";
    echo "Modalidad de trabajo: $modalidadTrabajo\n";
    echo "Salario minimo: $salarioMinimo\n";
    echo "Salario maximo: $salarioMaximo\n";
    echo "Escolaridad: $escolaridad\n";
    echo "Area de trabajo: $areaTrabajo\n";
    echo "Puesto de trabajo: $puestoTrabajo\n";
    echo "Ubicacion: $ubicacion\n";
    echo "Idioma: $idioma\n";
    echo "Nivel de idioma: $nivelIdioma\n";
    echo "Licencia de conducir: $licenciaConducir\n";
    echo "Años de experiencia: $anosExperiencia\n";

    // Insertar en la base de datos
    $conectar = conectarBD();
    if (!$conectar) {
        echo "No se pudo conectar a la base de datos\n";
        return;
    }

    $sql = "INSERT INTO perfiles (tipoContratacion, horarioTrabajo, modalidadTrabajo, sueldoMensualMinimo, sueldoMensualMaximo, escolaridad, area, puesto, ubicacion, idioma, nivelIdioma, licenciaConducir, añosExperiencia) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";
    $stmt = $conectar->prepare($sql);
    $params = [$tipoContratacion, $horarioTrabajo, $modalidadTrabajo, $salarioMinimo, $salarioMaximo, $escolaridad, $areaTrabajo, $puestoTrabajo, $ubicacion, $idioma, $nivelIdioma, $licenciaConducir, $anosExperiencia];
    if ($stmt->execute($params)) {
        echo "Los datos han sido insertados correctamente en la base de datos\n";
    } else {
        echo "Error al insertar los datos\n";
    }
    $conectar = null;
}

insertarDatos();
?>