# Funciones de evaluación de rendimiento 

def definir_estudiantes(lista_notas, nombre_estudiante, edad_estudiante, asignatura_estudiante, cantidad_notas):

    print("*** Gestión de rendimiento con Python ***\n")
    nombre_estudiante = str(input("Ingrese el nombre del estudiante: \n"))
    edad_estudiante = int(input("Ingrese la edad del estudiante: \n"))
    asignatura_estudiante = str(input("Ingrese la asignatura del estudiante: \n"))
    cantidad_notas = int(input("Ingrese una cantidad de notas a evaluar: \n"))
    print(f"A continuación, ingrese las {cantidad_notas} notas de {asignatura_estudiante}: ")

    for n in range(cantidad_notas):
        lista_notas = []
        nota = float(input(f"Ingrese la nota n°{n + 1}: "))
        lista_notas.append(nota)
        print ("Ingreso correcto!")

    return lista_notas, nombre_estudiante,edad_estudiante,asignatura_estudiante,cantidad_notas

def comparacionNotas(lista_notas, nombre_estudiante, edad_estudiante, asignatura_estudiante, cantidad_notas):
    print("Datos del estudiante: ")
    print(f"La lista completa de notas es: {lista_notas}")
    print(f"El nombre del usuario es: {nombre_estudiante}")
    print(f"La edad del estudiante es: {edad_estudiante}")
    print(f"La asignatura del estudiante es: {asignatura_estudiante}")
    print(f"La cantidad de notas ingresadas es: {cantidad_notas}")    