# Definimos una función de callback
def notificar_estado(alumno, estado):
    print(f"Notificación: {alumno['nombre']} ha {estado} con una calificación de {alumno['calificacion']}.")

# Función principal que procesa las calificaciones y usa el callback
def procesar_calificaciones(lista_alumnos, callback):
    for alumno in lista_alumnos:
        if alumno["calificacion"] >= 70:
            callback(alumno, "aprobado")  # Llamamos al callback con el estado "aprobado"
        else:
            callback(alumno, "reprobado")  # Llamamos al callback con el estado "reprobado"

# Lista de alumnos con sus nombres y calificaciones
alumnos = [
    {"nombre": "santos", "calificacion": 85},
    {"nombre": "wilbert", "calificacion": 92},
    {"nombre": "Rodney", "calificacion": 65},
    {"nombre": "Honorio", "calificacion": 95},
    {"nombre": "Guillermo", "calificacion": 78},
]

# Procesamos las calificaciones y usamos la función de callback
procesar_calificaciones(alumnos, notificar_estado)