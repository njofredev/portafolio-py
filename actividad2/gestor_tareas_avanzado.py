"""
Actividad n°2 "Gestión de lista de tareas mejorada"
Nicolás Jofré Andrade
14-02-2024

- Crear un archivo llamado 'gestor_tareas_avanzado.py'
- Implementa un sistema mejorado de gestión de tares que utilice 
diferentes tipos de datos y sentencias básicas de Python.
"""
# Import de funciones dentro de módulo funciones_gestor.py
import funciones_gestor
import datetime

lista_tareas = []
fecha_tarea = []

# Se llaman las funciones de funciones_gestor.py
while True:
    print("\n *** Gestor de tareas Avanzado con Python *** \n")
    print("1. Agregar tareas con fecha de ingreso")
    print("2. Mostrar tareas con detalles")
    print("3. Guarde las tareas en el archivo tareas.txt")
    print("4. Ingrese 0 para salir \n")
    opcion_menu = int(input("Ingrese una opción: \n"))

    if opcion_menu == 0:
        print("¡Gracias por participar en el gestor de tareas, vuelve pronto!")
        break
    elif opcion_menu == 1:
        funciones_gestor.agregar_tareas_con_fecha(lista_tareas, fecha_tarea)  
    elif opcion_menu == 2:
        funciones_gestor.mostrar_detalles_tareas(lista_tareas, fecha_tarea)
    elif opcion_menu == 3:
        funciones_gestor.completar_tareas()
    elif opcion_menu == 0:
        print("¡Gracias por participar en el gestor de tareas!")
    else:
        print("Ingrese un valor entre 0 y 3")
