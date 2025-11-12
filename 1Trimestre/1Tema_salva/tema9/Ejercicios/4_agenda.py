#Crea un script que funcione como una agenda telefónica
contactos = {}

def añadir_contacto(nombre,numero):
    if nombre in contactos:
        return "Ya existe un",nombre
    contactos[nombre] = numero
    return "Añadido correctamente"

def mostrar_contacto(nombre):
    if nombre in contactos:
        return "El numero de",nombre,"es",contactos[nombre]
    else:
        return nombre,"no esta en la agenda."
    
def eliminar_contacto(nombre):
    if nombre in contactos:
        del contactos[nombre]
        return nombre, "Eliminado correctamente"
    else:
        return "Ese nombre no esta en el diccionario"
    
print("Bienvenido a tu agenda")
continuar = True

while continuar:
    print("1.Añadir contacto")
    print("2.Mostrar contacto")
    print("3.Eliminar contacto")
    print("4.Salir")
    print("Elige una opcion:")
    opcion = int(input(""))

    if opcion == 1:
        nombre = input("Dime el nombre del contacto: ")
        numero = input("Dime el numero del contacto: ")
        print(añadir_contacto(nombre,numero))

    elif opcion == 2:
        nombre = input("Dime el nombre del contacto que quieres buscar: ")
        print(mostrar_contacto(nombre))

    elif opcion == 3:
        nombre = input("Dime el nombre del contacto que quieres eliminar: ")
        print(eliminar_contacto(nombre))
    elif opcion == 4:
        continuar = False
        print("Saliendo de la agenda...")