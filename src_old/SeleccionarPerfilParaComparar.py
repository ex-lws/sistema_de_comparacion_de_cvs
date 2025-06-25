# EXPLICACIÓN: 
# Este código permite seleccionar un perfil para ser usado como variable en la comparación.
# Debe de ya tenerse dado de alta en la tabla Perfiles de la base de datos embebida.

# VERSIÓN:
# Versión 1.0 del código. 13/05/2025.

#Metodo para recabar el ID del perfil a utilzar. Lo guarda en una variable entera y la retorna para ser usada.
def recabarIdParaSeleccionarPerfil():
    # Recabar el ID del perfil a eliminar
    id = input("Ingrese el ID del perfil a Utilizar para la comparación: ")
    if not id.isdigit():
        print("El ID debe ser un número entero.")
        return recabarIdParaSeleccionarPerfil()
    else:
        return id 