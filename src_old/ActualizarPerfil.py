# Este codigo permite editar un perfil.
 
# Versión 1.0 del código. 15/05/2025

# Importar las librerias y clases necesarias

def recabarIdParaEditarPerfil():
    # Recabar el ID del perfil a eliminar
    id = input("Ingrese el ID del perfil a actualizar: ")
    if not id.isdigit():
        print("El ID debe ser un número entero.")
        return recabarIdParaEditarPerfil()
    else:
        return id 
    
