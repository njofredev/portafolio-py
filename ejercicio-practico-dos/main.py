"""
Actividad n°2 - Ejercicio práctico
Cree un programa para ingresar notas de alumnos, el programa pregunta cuantos datos 
quiere ingresar el usuario y preguntar por la cantidad ingresada de datos.
Finalmente, que entregue como salida cuantas notas ingresadas son mayores que el promedio de ellas.
"""
# Se define una función para el ingreso de notas y su cantidad
def ingresarNotas():
    cantidad = int(input("Ingrese la cantidad de notas a promediar: ")) # Se declara "cantidad" y se le asigna el valor ingresado y posteriormente transformalo en 'int'
    notas = []     # Se inicializa la lista vacía notas para almacenar los datos ingresados
    sumaNotas = 0    # Se declara sumaNotas en valor 0

    for c in range(cantidad):    # Utilización de ciclo for para recorrer el rango de cantidad
        nota = float(input(f"Ingrese la nota {c + 1}: ")) # Se inicializa 'nota' transformando la petición de input() en el tipo de dato float (para manejar decimales) / 'c+1' indica que por cada vuelta el mensaje se le sumará 1
        notas.append(nota)        # Se agrega con append() la nota ingresada a la lista vacía 'notas'
        sumaNotas += nota        # A sumaNotas se le agrega la nota ingresada por el usuario en cada ciclo

    promedio = sumaNotas / cantidad    # Se saca el promedio de las notas con 'sumaNotas' dividiendolo por la 'cantidad' ingresada    
    notasMayorPromedio = len([nota for nota in notas if nota > promedio])    # len() adquiere la cantidad de elementos de la lista 'notasMayorPromedio'- Uso de chatGpt por la complejidad
    print(f"\nEl promedio de las notas ingresadas es: {promedio}")    # Finalmente, se le presenta al usuario el promedio de las notas ingresadas y la cantidad de notas mayores al promedio
    print(f"La cantidad de notas mayores que el promedio es: {notasMayorPromedio}")    # Se utiliza len() para conocer la longitud de la lista notasMayorPromedio y mostrar cuantas son mayor que el promedio

ingresarNotas() # Se inicia la función ingresarNotas()
