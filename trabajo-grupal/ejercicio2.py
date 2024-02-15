"""
Ejercicio 2 - Trabajo práctico grupal Python - njofre
'Ingreso de notas'

Realizar un programa que lea por teclado las 5 notas obtenidas por un alumno 
(comprendidas entre 0 y 10). A continuación, se debe mostrar todas las notas, la nota media,
la notas más alta que ha sacado y la nota menor
"""

for n in range(5):
    numIngresado = float(input("Ingrese un número entre 0 y 10"))
    
notas = []
notaMedia = 0
notaAlta = 0