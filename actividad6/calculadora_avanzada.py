"""
Actividad n°6 "Calculadora Avanzada"
Nicolás Jofré Andrade 
14-02-2024

- Crea un archivo llamada calculadora_avanzada.py
- Implementa un programa que funcione como una calculadora avanzada utilizando 
funciones en Python. Esta calculadora debe ser capaz de realizar operaciones básicas
y algunas operaciones avanzadas, como potenciación y raíz cuadrada.
"""
from funciones_avanzadas import *

while True:
    # Menú básico para la calculadora
    print("\n*** Calculadora avanzada con Python *** \n")
    print("Instrucciones: Ingrese una de las opciones a realizar. \n")
    print("1. Suma de dos números")
    print("2. Resta de dos números")
    print("3. Multiplicación de dos números")
    print("4. División de dos números") 
    print("5. Potencia de un números") 
    print("6. Raíz de un números") 
    print("5. Salir del programa \n")

    text_primer_numero = "Ingrese el primero número: "
    text_segundo_numero = "Ingrese el segundo número: "

    opcion = int(input("Ingrese una opción: \n"))

    if opcion == 1:
        num1 = int(input(text_primer_numero))
        num2 = int(input(text_segundo_numero))
        resultado_suma = sumarNumeros(num1,num2)
        print(f"\nEl resultado de la suma es: {resultado_suma}")
    elif opcion == 2:
        num1 = int(input(text_primer_numero))
        num2 = int(input(text_segundo_numero))
        resultado_resta = restarNumeros(num1,num2)
        print(f"\nEl resultado de la resta es: {resultado_resta}")
    elif opcion == 3:
        num1 = int(input(text_primer_numero))
        num2 = int(input(text_primer_numero))
        resultado_multiplicacion = multiplicarNumeros(num1,num2)
        print(f"\nEl resultado de la multiplicación es: {resultado_multiplicacion}")
    elif opcion == 4:
        num1 = int(input(text_primer_numero))
        num2 = int(input(text_segundo_numero))
        resultado_division = dividirNumeros(num1,num2)
        print(f"\nEl resultado de la división es: {resultado_division}")
    elif opcion == 5:
        print("Gracias por participar en la calculadora básica con Python!")
        break
    else:
        print("Ingrese un valor del menú indicado")