# EXPLICACIÓN: 
# Este código permite realizar la comparación entre la cantidad de CVS limpiados y un perfil seleccionado.
# Retorna una variable llamada resultados, que muestra los porcentajes de similitud.
# Arroja resultados por cada uno de ellos. (Ajustar el prompt)

# VERSIÓN:
# Versión 1.0 del código. 13/05/2025.

# Importar las librerías necesarias



from sentence_transformers import SentenceTransformer, util

# Carga el modelo MiniLM-L6-v2
modelo = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
 
def comparar_curriculums(curriculums, perfilEncontrado):
    """
    Compara la similitud entre el perfil y cada currículum usando embeddings y devuelve los porcentajes.
    """
    resultados = {}
    embedding_perfil = modelo.encode(perfilEncontrado, convert_to_tensor=True)
    for nombre, texto in curriculums.items():
        embedding_cv = modelo.encode(texto, convert_to_tensor=True)
        similitud = util.pytorch_cos_sim(embedding_perfil, embedding_cv).item()
        porcentaje = f"{round(similitud * 100, 2)} %"
        resultados[nombre] = porcentaje
    return resultados