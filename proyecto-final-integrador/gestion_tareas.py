"""
Proyecto final módulo 3
njofre 26-02-24
njofre

1. Crea un proyecto llamado "gestion_tareas.py"
2. Implementa un programa que permita:
    - gestionar_tareas()
    - evaluacion_rendimiento()
    - registro_contacto()
    - calculadora_avanzada()
"""
from funciones_integrador import *

while True:

    print("\n*** Bienvenid@ al multi-gestor de funciones *** ")
    print("Para continuar, elige una opción del siguiente menú: \n")
    print("(1) Gestionar tareas")
    print("(2) Evaluación de rendimiento de estudiantes")
    print("(3) Registro de contactos")
    print("(4) Calculadora avanzada")
    print("(5) Salir del programa")

    opcionMenu = int(input("Ingrese la opción: "))
    
    if opcionMenu == 1:
        gestionar_tareas()
    elif opcionMenu == 2:
        evaluacion_rendimiento()
    elif opcionMenu == 3:
        registro_contacto()
    elif opcionMenu == 4: 
        calculadora_avanzada()
    elif opcionMenu == 5:
        print("Gracias por participar del integrador de funciones! Saliendo...")
        break   
    else:
        print("ERROR: Ingrese una opción válida del menú mostrado")
