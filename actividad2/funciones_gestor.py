from funciones_gestor import * 

# Se definen las funciones mejoradas del gestor de tareas y sus parametros de entrada
def agregar_tareas_con_fecha(lista_tareas, fecha_tarea):
    cant_tareas = int(input("¿Cuántas tareas quieres agregar?: \n"))
    
    for n in range(cant_tareas):
        tarea = str(input(f"Ingrese la tarea n°{n + 1}: \n"))
        fecha = str(input("Ingrese la fecha de ingreso (dia/mes/año): \n"))
        lista_tareas.append(tarea)
        fecha_tarea.append(fecha)
    print("Tareas con fecha ingresadas correctamente")
    
def mostrar_detalles_tareas(lista_tareas, fecha_tarea):
    print(f"La cantidad de tareas ingresadas es: {len(lista_tareas)}")
    # Se recorre la lista lista_tareas[] y fecha_tarea[] con los datos ingresados
    for n in range(len(lista_tareas)):
        print(f"La tarea n°{n + 1} es: {lista_tareas[n]} y fue ingresada el: {fecha_tarea[n]}")
    
def completar_tarea(lista_tareas, fecha_tarea):
    if not lista_tareas:
        print("No hay tareas pendientes.")
        return
    
    print("Tareas pendientes:")
    for i, tarea in enumerate(lista_tareas, start=1):
        print(f"{i}. {tarea} - Fecha de ingreso: {fecha_tarea[i - 1]}")

    indice = int(input("Ingrese el número de la tarea que desea completar: "))
    if 0 < indice <= len(lista_tareas):
        tarea_completada = lista_tareas.pop(indice - 1)
        fecha_completada = fecha_tarea.pop(indice - 1)
        print(f"Tarea completada: {tarea_completada}, ingresada el {fecha_completada}")
    else:
        print("Número de tarea no válido.")
    
def guardar_tareas(lista_tareas, fecha_tarea):
    nombre_archivo = "tareas.txt"

    # Escribir las tareas en el archivo creado
    with open (nombre_archivo, "w") as archivo:
        for n in range(len(lista_tareas)):
            archivo.write(f"La tarea {lista_tareas[n]} fue ingresada el {fecha_tarea[n]}\n")
            
    
    print(f"Las tareas fueron exitosamente guardadas en {nombre_archivo}")

