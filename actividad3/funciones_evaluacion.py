# Funciones de evaluación de rendimiento 

def definir_estudiantes(lista_notas, nombre_estudiante, edad_estudiante, asignatura_estudiante, cantidad_notas):
    
    try:
        print("< Gestión de rendimiento de estudiante >\n")
        nombre = str(input("Ingrese el nombre del estudiante: \n"))
        nombre_estudiante.append(nombre)
        edad = int(input("Ingrese la edad del estudiante: \n"))
        edad_estudiante.append(edad)
        # Ingresar diferentes asignaturas
        asignatura = str(input("Ingrese la asignatura del estudiante: \n"))
        asignatura_estudiante.append(asignatura)
        cant_notas = int(input("Ingrese una cantidad de notas a evaluar: \n"))
        cantidad_notas.append(cant_notas)
        print(f"A continuación, ingrese las {cant_notas} notas de {nombre}: ")

        for n in range(cant_notas):
            nota = float(input(f"Ingrese la nota n°{n + 1}: "))
            lista_notas.append(nota)
            print ("Ingreso correcto!")
            
        #for m in range() / Cantidad de asignaturas
    except ValueError:
        print("ERROR: Ingrese un valor real.")

def mostrar_notas(lista_notas, nombre_estudiante, edad_estudiante, asignatura_estudiante, cantidad_notas):
    
    print("< Datos del estudiante: >")
    print(f"El nombre del usuario es: {nombre_estudiante[0]}")
    print(f"La edad del estudiante es: {edad_estudiante[0]}")
    print(f"La asignatura del estudiante es: {asignatura_estudiante[0]}")
    print(f"La cantidad de notas ingresadas es: {cantidad_notas}")
    print(f"La lista completa de notas es: {lista_notas}") 
    
def comparacion_notas(lista_notas, nombre_estudiante, asignatura_estudiante):

    aprobado = True
    reprobado = False
    
    for n in range(len(lista_notas)):
        promedio = sum(lista_notas) / len(lista_notas)
    
    print(f"Las notas son: {lista_notas} \n")    
    print(f"El promedio de notas es:{promedio} ")    

    if promedio >= 4.0:
        print(f"Tu promedio ({promedio}) de {asignatura_estudiante} -  califica como APROBADO")
        estado = aprobado
    elif promedio <= 3.9:
        print(f"Tu promedio {promedio} califica como REPROBADO")
        estado = reprobado
    
    if estado == True:
        print(f"¡Felicitaciones {nombre_estudiante[0]}, has aprobado {asignatura_estudiante[0]}:) !")
    else:
        print(f"¡Lo sentimos {nombre_estudiante[0]}, has reprobado {asignatura_estudiante[0]} :(!")

"""
sum: 
Falta ingresar for para la cantidad de asignaturas - agregar asignaturas
Todas las otras funciones están listas
"""