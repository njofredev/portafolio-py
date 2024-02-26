import math

# Se definen las funciones del integrador

#1. Definición de gestión de tareas
def gestionar_tareas():

    lista_tareas = []

    def agregar_tarea():
        try:
            cant_tareas = int(input("¿Cuántas tareas quieres agregar?: \n"))
        except ValueError:
            print("ERROR: Ingrese un valor numérico")

        for c in range(cant_tareas):
            tarea = str(input("Ingrese la tarea: \n"))
            lista_tareas.append(tarea)

        print("¡Las tareas se agregaron correctamente!")
        print(f"Las tareas agregadas son: {lista_tareas}")

    def mostrar_tareas():
        print(f"\nHasta el momento has agregado: {len(lista_tareas)} tareas")
        print("Las tareas ingresadas hasta el momento son: ",lista_tareas)

    def guardar_tareas():
        nombre_archivo = "tareas.txt"

        with open (nombre_archivo, "w") as archivo:
            for n in lista_tareas:
                archivo.write(n + "\n")
        
        print(f"Las tareas fueron exitosamente guardadas en {nombre_archivo}")

    while True:
        print("\n *** Gestor de tareas con Python *** \n")
        print("1. Agregar tareas")
        print("2. Mostrar tareas")
        print("3. Guarde las tareas en el archivo tareas.txt")
        print("4. Ingrese 0 para salir \n")
        opcion_menu = int(input("Ingrese una opción: \n"))

        if opcion_menu == 0:
            print("¡Gracias por participar en el gestor de tareas, vuelve pronto!")
            break
        elif opcion_menu == 1:
            agregar_tarea()  
        elif opcion_menu == 2:
            mostrar_tareas()
        elif opcion_menu == 3:
            guardar_tareas()
        elif opcion_menu == 0:
            print("¡Gracias por participar en el gestor de tareas!")
        else:
            print("Ingrese un valor entre 0 y 3")
    
# 2. Definición de evaluación de rendimiento de estudiantes
def evaluacion_rendimiento():


    def agregar_tareas_con_fecha(lista_tareas, fecha_tarea):
        cant_tareas = int(input("¿Cuántas tareas quieres agregar?: \n"))
        
        for n in range(cant_tareas):
            tarea = str(input(f"Ingrese la tarea n°{n + 1}: \n"))
            fecha = str(input("Ingrese la fecha de ingreso (dia/mes/año): \n"))
            lista_tareas.append(tarea)
            fecha_tarea.append(fecha)
        print("Tareas con fecha ingresadas correctamente")
        
    def mostrar_detalles_tareas(lista_tareas, fecha_tarea):
        print(f"La cantidad de tareas ingresadas es: {len(lista_tareas)}")

        for n in range(len(lista_tareas)):
            print(f"La tarea n°{n + 1} es: {lista_tareas[n]} y fue ingresada el: {fecha_tarea[n]}")
        
    def completar_tarea(lista_tareas, fecha_tarea):
        if not lista_tareas:
            print("No hay tareas pendientes.")
            return
        
        print("Tareas pendientes:")
        for i, tarea in enumerate(lista_tareas, start=1):
            print(f"{i}. {tarea} - Fecha de ingreso: {fecha_tarea[i - 1]}")

        indice = int(input("Ingrese el número de la tarea que desea completar: "))
        if 0 < indice <= len(lista_tareas):
            tarea_completada = lista_tareas.pop(indice - 1)
            fecha_completada = fecha_tarea.pop(indice - 1)
            print(f"Tarea completada: {tarea_completada}, ingresada el {fecha_completada}")
        else:
            print("Número de tarea no válido.")
        
    def guardar_tareas(lista_tareas, fecha_tarea):
        nombre_archivo = "tareas.txt"

        with open (nombre_archivo, "w") as archivo:
            for n in range(len(lista_tareas)):
                archivo.write(f"La tarea {lista_tareas[n]} fue ingresada el {fecha_tarea[n]}\n")
                
        
        print(f"Las tareas fueron exitosamente guardadas en {nombre_archivo}")

    lista_tareas = []
    fecha_tarea = []

    while True:
        print("\n *** Gestor de tareas Avanzado con Python *** \n")
        print("1. Agregar tareas con fecha de ingreso")
        print("2. Mostrar tareas con detalles")
        print("3. Completar tareas ingresadas")
        print("4. Guardar tareas en tareas.txt")
        print("5. Salir del programa \n")
        opcion_menu = int(input("Ingrese una opción: \n"))

        if opcion_menu == 5:
            print("¡Gracias por participar en el gestor de tareas, vuelve pronto!")
            break
        elif opcion_menu == 1:
            agregar_tareas_con_fecha(lista_tareas, fecha_tarea)  
        elif opcion_menu == 2:
            mostrar_detalles_tareas(lista_tareas, fecha_tarea)
        elif opcion_menu == 3:
            completar_tarea(lista_tareas, fecha_tarea)
        elif opcion_menu == 4:
            guardar_tareas(lista_tareas, fecha_tarea)
        else:
            print("Ingrese un valor entre 0 y 5")


# 3. Se define función para el registro de contactos
def registro_contacto():
    
    class Contacto:
        def __init__(self, nombre, telefono, email):
            self.nombre = nombre
            self.telefono = telefono
            self.email = email

    def agregar_contacto():
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el teléfono del contacto: ")
        email = input("Ingrese el email del contacto: ")
        contacto = Contacto(nombre, telefono, email)
        contactos.append(contacto)
        print("Contacto agregado correctamente.")

    def mostrar_contactos():
        if not contactos:
            print("No hay contactos para mostrar.")
        else:
            print("Lista de contactos:")
            for i, contacto in enumerate(contactos, 1):
                print(f"{i}. Nombre: {contacto.nombre}, Teléfono: {contacto.telefono}, Email: {contacto.email}")

    contactos = []

# Menú
    while True:
        print("\n *** Gestor de contactos con Python *** \n")
        print("1. Agregar contacto")
        print("2. Mostrar contactos")
        print("3. Salir del programa")
        
        opcion_menu = input("Seleccione una opción: ")

        if opcion_menu == "1":
            agregar_contacto()
        elif opcion_menu == "2":
            mostrar_contactos()
        elif opcion_menu == "3":
            print("¡Gracias por participar en el gestor de tareas!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

# 4. Definición de función calculadora avanzada
def calculadora_avanzada():
    
    def sumarNumeros(a,b):
        return a+b

    def restarNumeros(a,b):
        return a-b

    def multiplicarNumeros(a,b):
        return a*b

    def dividirNumeros(a,b):
        return a/b

    def potenciaNumero (a,b):
        return a**b

    def raizNumero (a): # Se usa math.sqrt para sacar la raiz cuadrada del num ingresado
        raiz_cuadrada = math.sqrt(a)
        return a

    while True:
        # Menú básico para la calculadora
        print("\n*** Calculadora avanzada con Python *** \n")
        print("Instrucciones: Ingrese una de las opciones a realizar. \n")
        print("1. Suma de dos números")
        print("2. Resta de dos números")
        print("3. Multiplicación de dos números")
        print("4. División de dos números") 
        print("5. Potencia de un número") 
        print("6. Raíz de un número") 
        print("7. Salir del programa \n")

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
            num1 = int(input(text_primer_numero))
            num2 = int(input("Ingrese el exponente para la potencia: "))
            resultado_potencia = potenciaNumero(num1,num2)
            print(f"\nEl resultado de la potencia es: {resultado_potencia}")
        elif opcion == 6:
            num1 = int(input(text_primer_numero))
            resultado_raiz = raizNumero(num1)
            print("La raíz cuadrada de", num1, "es:", resultado_raiz)

        elif opcion == 7:
            print("Gracias por participar en la calculadora avanzada con Python!")
            break
        else:
            print("Ingrese un valor del menú indicado")
