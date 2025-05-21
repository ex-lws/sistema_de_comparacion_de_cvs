<?php
<?php
// Este código permite ver los perfiles registrados en la base de datos. 
// Versión 1.1 del código. 21/05/2025
// Reconversion a PHP.

require_once 'ConectarBD.php'; // Método para conectarnos a la base de datos

function verPerfiles() {
    // Conectamos a la base de datos
    $conectar = conectarBD();
    if (!$conectar) {
        echo "No se pudo conectar a la base de datos\n";
        return;
    }

    try {
        $sql = "SELECT * FROM perfiles";
        $stmt = $conectar->query($sql);
        $resultados = $stmt->fetchAll(PDO::FETCH_ASSOC);

        foreach ($resultados as $resultado) {
            print_r($resultado);
        }
    } catch (PDOException $e) {
        echo "Error al ejecutar la consulta: " . $e->getMessage() . "\n";
    } finally {
        $conectar = null;
    }
}

verPerfiles();
?>