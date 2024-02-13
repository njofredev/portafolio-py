"""
Ejercicio 2 - Trabajo práctico grupal Python - njofre
'Ingreso de notas'

Realizar un programa que lea por teclado las 5 notas obtenidas por un alumno 
(comprendidas entre 0 y 10). A continuación, debe mostrar todas las notas, la nota media,
la notas más alta que ha sacado y la nota menor.
"""

def ingresoNotas():
    contador = 1
    notaIngresada = []
    notaMenor = []
    notaAlta = []
    
    while contador <= 5:
        notaIngresada.append(int(input(f"Ingrese la nota n° {contador} \n")))
        contador += 1
        
    for c in notaIngresada:
        print(c)
    mediana = sorted(notaIngresada)
    
    print("Todas las notas ingresadas son: \n")
    print(mediana)

        
    
ingresoNotas()

# Terminar desarrollo quedé en imprimir la mediana de los números ingresados 