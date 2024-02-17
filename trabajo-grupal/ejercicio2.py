"""
Ejercicio 2 - Trabajo práctico grupal Python - njofre
'Ingreso de notas'

Realizar un programa que lea por teclado las 5 notas obtenidas por un alumno 
(comprendidas entre 0 y 10). A continuación, se debe mostrar todas las notas, la nota media,
la notas más alta que ha sacado y la nota menor.
"""

notas = [] # Se inicializa la lista de notas

for n in range(5): # Se recorre las 5 notas por ingresar
    numIngresado = float(input("Ingrese un número entre 0 y 10 \n"))
    
    if numIngresado < 0 or numIngresado > 10:
        print("ERROR: Ingrese un número en 0 y 10 \n")
    else:
        notas.append(numIngresado)
        print("Ingreso correcto!")    
     
notaAlta = max(notas)
notaBaja = min(notas)
notaMedia = sum(notas) / 5

print(f"Todas las notas son: {notas}")    
print(f"La nota mayor es {notaAlta} y la nota menor es {notaBaja} y la nota promedio es: {notaMedia} ")

