# EXPLICACIÓN: 
# Este código permite realizar la comparación entre la cantidad de CVS limpiados y un perfil seleccionado.
# Retorna una variable llamada resultados, que muestra los porcentajes de similitud.
# Arroja resultados por cada uno de ellos. (Ajustar el prompt)

# VERSIÓN:
# Versión 1.0 del código. 13/05/2025.

# Importar las librerías necesarias



from sentence_transformers import SentenceTransformer, util
import os

# Carga el modelo MiniLM-L6-v2
modelo = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def comparar_curriculums(curriculums, perfilEncontrado):
    """
    Compara la similitud entre el perfil y cada currículum usando embeddings y devuelve los porcentajes
    solo para aquellos mayores a 80%.
    """
    resultados = {}
    embedding_perfil = modelo.encode(perfilEncontrado, convert_to_tensor=True)
    for nombre, texto in curriculums.items():
        embedding_cv = modelo.encode(texto, convert_to_tensor=True)
        similitud_tensor = util.pytorch_cos_sim(embedding_perfil, embedding_cv)
        similitud = similitud_tensor[0][0].item()  # Extrae el valor escalar
        similitud_normalizada = (similitud + 1) / 2
        porcentaje_num = round(similitud_normalizada * 100, 2)
        if porcentaje_num >= 80.0:
            resultados[nombre] = f"{porcentaje_num} %"
    return resultados

def mostrarResultadosTrasComparacion(resultados):
    for ruta, porcentaje in resultados.items():
        print(f"\n📄 RUTA RELATIVA: {ruta}")
        print(f"SIMILITUD: {porcentaje}")


# Función para extraer nombre desde el nombre del archivo
def extraer_nombre_candidato(nombre_archivo):
    nombre_base = os.path.basename(nombre_archivo)
    nombre_sin_extension = os.path.splitext(nombre_base)[0]
    partes = nombre_sin_extension.split('_')

    if len(partes) >= 3 and partes[0].strip().upper() == "CV":
        return ' '.join(partes[1:-1]).strip()
    else:
        return "Desconocido"

