# EXPLICACIÓN: 
# Este código permite poder ingresar un ID para posteriormente usarlo y actualizar un perfil vía SQL.

# VERSIÓN:
# Versión 1.5 del código. 15/05/2025.

# Permite recabar un ID y guardarlo en una variable para posteriormente usarlo con su retorno en la actualización de un perfil.
# El mensaje es personalizado.
def recabarIdParaEditarPerfil():
    # Recabar el ID del perfil a eliminar
    id = input("Ingrese el ID del perfil a actualizar: ")
    if not id.isdigit():
        print("El ID debe ser un número entero.")
        return recabarIdParaEditarPerfil()
    else:
        return id 
    
