# #Este codigo permite agregar un nuevo perfil al sistema

#Versión 1.0 del código. 21/05/2025


def recabarIdParaEliminarPerfil():
    # Recabar el ID del perfil a eliminar
    id = input("Ingrese el ID del perfil a eliminar: ")
    if not id.isdigit():
        print("El ID debe ser un número entero.")
        return recabarIdParaEliminarPerfil()
    else:
        return id 
