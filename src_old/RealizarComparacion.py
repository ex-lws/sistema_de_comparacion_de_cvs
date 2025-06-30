# EXPLICACIÓN: 
# Este código permite realizar la comparación entre la cantidad de CVS limpiados y un perfil seleccionado.
# Retorna una variable llamada resultados, que muestra los porcentajes de similitud.
# Arroja resultados por cada uno de ellos. (Ajustar el prompt)

# VERSIÓN:
# Versión 2.0 del código. 25/05/2025.

# Importar las librerías necesarias
from sentence_transformers import SentenceTransformer, util
import os

# Carga el modelo MiniLM-L6-v2.
modelo = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
# Limite del porcentaje de similitud para mostrar  e ingestar al diccionario resultados.
porcentajeSimulitd = 50.0

# Este método permite comparar un perfil con los curriculums.
# Requiere como parámetros un diccionario con las rutas relativas de los cvs temporale y su texto extraído y limpiado.
# Requiere también el perfil que se quiere comparar, previamente extraido y guardado en una variable.
def comparar_curriculums(curriculums, perfilEncontrado, porcentajeSimilitud):
    """
    Compara la similitud entre el perfil y cada currículum usando embeddings y devuelve los porcentajes.
    Solo incluye resultados iguales o mayores al porcentajeSimilitud dado.
    """
    resultados = {}
    embedding_perfil = modelo.encode(perfilEncontrado, convert_to_tensor=True)
    for nombre, texto in curriculums.items():
        embedding_cv = modelo.encode(texto, convert_to_tensor=True)
        similitud_tensor = util.pytorch_cos_sim(embedding_perfil, embedding_cv)
        similitud = similitud_tensor[0][0].item()
        similitud_normalizada = (similitud + 1) / 2
        porcentaje_cv = round(similitud_normalizada * 100, 2)
        if porcentaje_cv >= porcentajeSimilitud:
            resultados[nombre] = f"{porcentaje_cv} %"
    return resultados

# Este método permite mostrar los resultados de la comparación en la consola.
def mostrarResultadosTrasComparacion(resultados):
    for ruta, porcentaje in resultados.items():
        print(f"\n📄 RUTA RELATIVA: {ruta}")
        print(f"SIMILITUD: {porcentaje}")



