"""
Actividad n°1 "Manejo de lista de tareas"
Nicolás Jofré Andrade
19-02-2024

- Crear un archivo llamado 'gestor_tareas.py'
- Implementar 4 funciones:
    - agregar_tarea()
    - mostrar_tareas()
    - completar_tarea()
    - guardar_tareas()
- Guardar el archivo y ejecútalo para ver como se gestionan las tareas.
- Cómo se se completan y se guardan en un archivo de texto llamado:
    - tareas.txt
"""
# Inicialización de variable que almacena la lista de tareas agregadas en la función agregar_tareas()
lista_tareas = []

# 1. Ingreso de tareas
def agregar_tarea():
    try:
        cant_tareas = int(input("¿Cuántas tareas quieres agregar?: \n"))
    except ValueError:
        print("ERROR: Ingrese un valor numérico")

    for c in range(cant_tareas):
        tarea = str(input("Ingrese la tarea: \n"))
        lista_tareas.append(tarea)

    print("¡Las tareas se agregaron correctamente!")
    print(f"Las tareas agregadas son: {lista_tareas}")

# 2. Mostrar tareas ingresadas
def mostrar_tareas():
    print(f"\n Hasta el momento has agregado: {len(lista_tareas)} tareas")
    print("Las tareas ingresadas hasta el momento son: ",lista_tareas)

# 3. Completar tareas | Si la tarea está incompleta = 0 , si está completa = 1
def completar_tareas(): 
    print("Completar tareas")

# 4. Se guarda la tarea en un archivo de texto
def guardar_tareas():
    nombre_archivo = "tareas.txt"

    # Escribir las tareas en el archivo creado
    with open (nombre_archivo, "w") as archivo:
        for n in lista_tareas:
            archivo.write(n + "\n")
    
    print(f"Las tareas fueron exitosamente guardadas en {nombre_archivo}")

# Menú de script
while True:
    print("\n *** Gestor de tareas con Python *** \n")
    print("1. Agregar tareas")
    print("2. Mostrar tareas")
    print("3. Guarde las tareas en el archivo tareas.txt")
    print("4. Ingrese 0 para salir \n")
    opcion_menu = int(input("Ingrese una opción: \n"))

    if opcion_menu == 0:
        print("¡Gracias por participar en el gestor de tareas, vuelve pronto!")
        break
    elif opcion_menu == 1:
        agregar_tarea()  
    elif opcion_menu == 2:
        mostrar_tareas()
    elif opcion_menu == 3:
        guardar_tareas()
    elif opcion_menu == 0:
        print("¡Gracias por participar en el gestor de tareas!")
    else:
        print("Ingrese un valor entre 0 y 3")
    
    