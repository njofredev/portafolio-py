import datetime

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
    
def completar_tareas():
    print("Aquí se pueden completar las tareas ingresadas")
    
def guardar_tareas():
    print("Aquí se guardan las tareas")

