"""
Ejercicio 1 - Trabajo práctico grupal Python - njofre
'Ingreso de números pares e impares'

Al ingresar un número par cualquiera que sea del 2 al 100, este imprima en pantalla
todos los números pares siguientes, y si ingreso un número impar cualquiera sea del 
1 al 99 se imprima en pantalla todos los números impares siguientes hasta el 99. 
Si ingreso el 0 o un número menor y si ingreso un número mayor al 100, el programa
debe enviar un mensaje de que no es posible realizarlo y volver a preguntar por el 
ingreso del número. 
"""

def ingresoNum():
    while True:
        try:
            numIngresado = int(input("Ingrese un número entre el 2 y el 100 | 0 para salir \n"))
            
            if numIngresado == 0:
                print("Gracias por participar!")
                break    

            if numIngresado < 2 or numIngresado > 100:
                print("ERROR: Ingrese un número mayor a 2 y menor que 100 \n")
            else:
                if numIngresado % 2 == 0: # Número par
                    for n in range(numIngresado + 2, 101, 2): 
                        numIngresado += 2
                        print(f"El siguiente número par es: {numIngresado}")
                else:                     # Número impar
                    for n in range(numIngresado + 1, 100, 2):
                        numIngresado += 2
                        print(f"El siguiente número impar es: {numIngresado}")    
                 
        except ValueError:
            print("ERROR: Ingrese un valor numérico")
            
ingresoNum()
