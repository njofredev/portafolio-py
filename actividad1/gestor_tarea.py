"""
Actividad n°1 "Manejo de lista de tareas"
Nicolás Jofré Andrade
14-02-2024

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
# Se definen las 4 funciones pedidas
# 1. Ingreso de tareas
def agregar_tarea(tarea, listaTareas):
    listaTareas.append(tarea) # Se agrega la tarea ingresada
    print("La tarea se agregó correctamente") 

# 2. Mostrar tareas ingresadas
def mostrar_tareas(listaTareas):
    if listaTareas:
        print("Lista de tareas: ")
        for i, tarea in enumerate(listaTareas, start = 1):
            print(f"{i}. {tarea}")
    else:
        print("No hay tareas pendientes.")

def completar_tarea():
    print ("Se ingresa a la función completar_tarea()")

# Se guarda la tarea en un archivo de texto
def guardar_tareas():
    print("Se ingresa la función guardar_tareas()")

# Inicio de programa 
while True:
    print("\n *** Gestor de tareas con Python ***")
    

# Inicialización de las 4 funciones
"""agregar_tarea()
mostrar_tareas()
completar_tarea()
guardar_tareas()"""