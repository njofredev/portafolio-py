# Funciones de evaluación de rendimiento 

def definir_estudiantes():

    print("*** Gestión de rendimiento con Python ***\n")
    nombre_estudiante = str(input("Ingrese el nombre del estudiante: "))
    edad_estudiante = int(input("Ingrese la edad del estudiante: "))
    asignatura_estudiante = str(input("Ingrese la asignatura del estudiante: "))
    print(f"A continuación, ingrese las 5 notas de {asignatura_estudiante}: ")

    for n in range(5):
        lista_notas = []
        nota = int(input(f"Ingrese la nota n°{n + 1}: "))
        lista_notas.append(nota)
        print ("Ingreso correcto!")

    return lista_notas