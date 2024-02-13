"""
Ejercicio 2 - Trabajo práctico grupal Python - njofre
'Ingreso de notas'

Realizar un programa que lea por teclado las 5 notas obtenidas por un alumno 
(comprendidas entre 0 y 10). A continuación, debe mostrar todas las notas, la nota media,
la notas más alta que ha sacado y la nota menor.
"""

def ingresoNotas():
    notas = []
    for i in range(5):
        nota = float(input(f"Ingrese la nota {i + 1}: \n"))
        while nota < 0 or nota > 10:
            print("La nota debe estar entre 0 y 10.")
            nota = float(input(f"Ingrese la nota {i + 1}: \n"))
        notas.append(nota)

    # sum() suma todas las notas, len() obtiene la cantidad de notas de la lista, max() obtiene el número máximo de la lista, min() obtiene el menor de la lista
    notaMedia = sum(notas) / len(notas)
    notaMaxima = max(notas)
    notaMinima = min(notas)

    print("\nTodas las notas son:", notas)
    print("La nota media es:", notaMedia)
    print("La nota más alta es:", notaMaxima)
    print("La nota más baja es:", notaMinima)

ingresoNotas()