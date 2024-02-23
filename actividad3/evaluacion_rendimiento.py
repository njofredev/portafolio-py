"""
Actividad n°3 "Evaluación de rendimiento del estudiante"
Nicolás Jofré Andrade 
14-02-2024

- Crea un archivo llamado 'evaluacion_rendimiento.py'
- Implementa un programa que evalúe el rendimiento de un estudiante
según sus calificaciones en diferentes asignaturas.
- Funciones:
    - definir_estudiantes()
    - mostrar_notas()
"""
from funciones_evaluacion import * 


# Atributos iniciales de estudiantes
lista_notas = []
nombre_estudiante = []
edad_estudiante = []
asignatura_estudiante = []
cantidad_notas = []

#Inicio de programa
while True:
    print("\n *** Evaluación de rendimiento *** \n")
    print("1. Ingresar un estudiante")
    print("2. Detalles de estudiante")
    print("3. Rendimiento de notas ingresadas")
    print("4. Salir del programa \n")
    opcion_menu = int(input("Ingrese una opción: \n"))

    if opcion_menu == 5:
        print("¡Gracias por participar en el gestor de rendimiento, vuelve pronto!")
        break
    elif opcion_menu == 1:
        definir_estudiantes(lista_notas, nombre_estudiante, edad_estudiante, asignatura_estudiante, cantidad_notas) 
    elif opcion_menu == 2:
        mostrar_notas(lista_notas, nombre_estudiante, edad_estudiante, asignatura_estudiante, cantidad_notas)
    elif opcion_menu == 3:
        comparacion_notas(lista_notas, nombre_estudiante, asignatura_estudiante)
    else:
        print("Ingrese un valor entre 0 y 5")