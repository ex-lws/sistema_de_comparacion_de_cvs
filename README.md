# Sistema de Comparación entre Currículums Vitae y Vacantes Profesionales

Este proyecto es un sistema para realizar comparaciones entre currículums vitae y perfiles profesionales, vacantes o puestos de trabajo.  
Los resultados tras la comparación muestran aquellos candidatos o currículums que están más cercanos al perfil profesional.

El beneficio más grande es evitar la revisión manual de muchos —incluso cientos— de archivos, quedando únicamente los más parecidos, basándose en los criterios de la vacante.  
Además, el usuario puede seleccionar el porcentaje de similitud deseado antes de realizar un proceso de comparación, en busca de mejores resultados.  

Uno de los aspectos más destacados del sistema es que utiliza una base de datos embebida (no requiere un gestor externo), y por otro lado, hace uso de un modelo de lenguaje para realizar comparaciones entre los elementos principales del proyecto.

El sistema fue desarrollado primeramente en su versión de consola, para luego dar paso a la versión con interfaz gráfica.

El proceso de desarrollo se llevó a cabo de manera colaborativa.

---

## Características

- Posibilidad de subir al sistema uno o varios archivos PDF (currículums).
- Módulos para ingresar o dar de alta las diferentes vacantes, perfiles profesionales o puestos de trabajo.
- Posibilidad de actualizar y eliminar los perfiles profesionales ya registrados en la base de datos.
- Módulo de comparación, donde el usuario puede seleccionar el perfil que desea comparar y el porcentaje mínimo de similitud para considerar aptos a los candidatos.
- Visualización de los resultados tras los procesos de comparación, incluyendo la opción de descargar los currículums que hayan pasado el umbral de similitud.
- Opciones de configuración orientadas al correcto manejo de los datos, la eficiencia y el buen funcionamiento del sistema.

---

## Tecnologías utilizadas

- **Lenguaje de programación:** Python 3.12
- **Framework para la interfaz gráfica:** PyQt6, PyQt6-tools, Qt Designer
- **Base de datos:** SQLite
- **Librerías destacadas:** `sentence-transformers`, `pdfminer.six`

---

## Cómo usar

Este proyecto incluye un entorno virtual preconfigurado. Las librerías requeridas se encuentran también listadas en el archivo `requirements.txt`.

1. Clona este repositorio.
2. Si deseas recrear el entorno virtual:
   - Genera uno con `python -m venv entornoVirtualWindows`
   - Actívalo con `.\entornoVirtualWindows\Scripts\activate`
   - Instala las dependencias con `pip install -r requirements.txt`
3. Ejecuta `menuPrincipal.py`
4. Opcional: El sistema incluye datos "dummy" que puedes usar para propósitos de prueba o experimentación.

---

## Capturas de pantalla
 
### Interfaz principal
![Menú principal](Screenshots/menuPrincipalSS.png)

### Modulo de opciones de configuración
![Modulo de opciones de configuración](Screenshots/menuConfiguracionSS.png)

### Mostrar todas las vacantes registradas
![Modulo para mostrar todas las vacantes registradas](Screenshots/menuVerVacantes.png)

### Registrar una vacante
![Modulo para dar de alta una vacante o perfil profesional](Screenshots/menuAgregarVacantesSS.png)

### Editar o actualizar una vacante
![Modulo para editar una vacante o perfil profesional](Screenshots/menuEditarVacanteSS.png)

### Eliminar una vacante
![Modulo para eliminar una vacante o perfil profesional](Screenshots/meenuEliminarVacante.png)

### Comparar curriculums vitae contra una vacante
![Modulo para comparar una vacante o perfil profesional con varios CVS](Screenshots/menuComparacionSS.png)

### Consultar los resultados tras una comparación
![Ver y descargar los resultados favorables tras la comparación](Screenshots/menuVerResultadosSS.png)


