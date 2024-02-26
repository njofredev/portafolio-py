"""
Actividad n°5 "Registro de contactos" 
Nicolás Jofré Andrade  
14-02-2024

- Crea un archivo llamado 'registro_contactos.py'
- Implementa un programa que permita a los usuarios gestionar un registro de 
contactos utilizando diversas estructuras de datos en Python.

funciones: agregar_contacto(), mostrar_contacto(), salir()
"""
# Clase contacto
class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

def agregar_contacto():
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el teléfono del contacto: ")
    email = input("Ingrese el email del contacto: ")
    contacto = Contacto(nombre, telefono, email)
    contactos.append(contacto)
    print("Contacto agregado correctamente.")

def mostrar_contactos():
    if not contactos:
        print("No hay contactos para mostrar.")
    else:
        print("Lista de contactos:")
        for i, contacto in enumerate(contactos, 1):
            print(f"{i}. Nombre: {contacto.nombre}, Teléfono: {contacto.telefono}, Email: {contacto.email}")

# Lista para almacenar los contactos
contactos = []

# Menú
while True:
    print("\n *** Gestor de contactos con Python *** \n")
    print("1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Salir del programa")
    
    opcion_menu = input("Seleccione una opción: ")

    if opcion_menu == "1":
        agregar_contacto()
    elif opcion_menu == "2":
        mostrar_contactos()
    elif opcion_menu == "3":
        print("¡Gracias por participar en el gestor de tareas!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
