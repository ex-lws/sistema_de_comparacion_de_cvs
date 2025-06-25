# EXPLICACIÓN: 
# Este código permite guardar en una variable en ID de un perfil a eliminar.

# VERSIÓN:
# Versión 1.5 del código. 05/06/2025.

# Permite recabar un ID y guardarlo en una variable para posteriormente usarlo con su retorno en la eliminación de un perfil.
# El mensaje es personalizado.
def recabarIdParaEliminarPerfil():
    # Recabar el ID del perfil a eliminar
    id = input("Ingrese el ID del perfil a eliminar: ")
    if not id.isdigit():
        print("El ID debe ser un número entero.")
        return recabarIdParaEliminarPerfil()
    else:
        return id 
