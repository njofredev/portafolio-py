"""
Ejercicio 3 - Trabajo práctico grupal Python - njofre
'Meses'

Crea un programa que pida al usuario un número de mes (por ejemplo, el 4) y el script diga cuántos días
tiene (por ejemplo, 30 días) y entregue el nombre del mes ingresado. Debes usar listas. Febrero tiene 28 días.
"""
# Son 12 meses, se incluye el índice 0 para controlar las excepciones incorrectas
meses = ['no existe','Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
diasPorMes = [0,31,28,31,30,31,30,31,31,30,31,30,31]

print("Conoce cuantos días tiene el mes!")
# Pedimos un número al usuario
mesIngresado = int(input("Ingrese un número de mes: \n"))

# Pregunta si el número que ingresa el usuario es mayor a 0 y menor o igual a 12
if mesIngresado > 0 and mesIngresado <=12:
    #f-string para comparar de la lista 'meses' en el index con el 'mesIngresado' por el usuario
    print(f"El nombre del mes ingresado es: {meses[mesIngresado]} y tiene: {diasPorMes[mesIngresado]} días.")
else:
    print(f"El mes {meses[0]} y tiene {diasPorMes[0]} días.")

