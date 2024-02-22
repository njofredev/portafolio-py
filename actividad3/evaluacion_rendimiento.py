"""
Actividad n°3 "Evaluación de rendimiento del estudiante"
Nicolás Jofré Andrade 
14-02-2024

- Crea un archivo llamado 'evaluacion_rendimiento.py'
- Implementa un programa que evalúe el rendimiento de un estudiante
según sus calificaciones en diferentes asignaturas.
"""
from funciones_evaluacion import * 


# Definición de estudiantes
lista_notas = []
nombre_estudiante = ""
edad_estudiante = 0
asignatura_estudiante = ""
cantidad_notas = 0

definir_estudiantes(lista_notas, nombre_estudiante, edad_estudiante, asignatura_estudiante, cantidad_notas)

comparacionNotas(lista_notas, nombre_estudiante, edad_estudiante, asignatura_estudiante, cantidad_notas)