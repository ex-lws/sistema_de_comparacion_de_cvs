#Metodo para recabar el ID del perfil a utilzar
def recabarIdParaSeleccionarPerfil():
    # Recabar el ID del perfil a eliminar
    id = input("Ingrese el ID del perfil a Utilizar: ")
    if not id.isdigit():
        print("El ID debe ser un número entero.")
        return recabarIdParaSeleccionarPerfil()
    else:
        return id 