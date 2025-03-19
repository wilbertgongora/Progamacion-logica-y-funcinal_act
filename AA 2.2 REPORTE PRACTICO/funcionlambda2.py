# Lista de alumnos con sus nombres y calificaciones
alumnos = [
    {"nombre": "Juan", "calificacion": 85},
    {"nombre": "Jacobo", "calificacion": 92},
    {"nombre": "Guillermo", "calificacion": 78},
    {"nombre": "Honorio", "calificacion": 95},
    {"nombre": "santos", "calificacion": 88},
]

# Ordenar los alumnos por calificación (de menor a mayor)
alumnos_ordenados = sorted(alumnos, key=lambda x: x["calificacion"])

print("Alumnos ordenados por calificación:")
for alumno in alumnos_ordenados:
    print(f"{alumno['nombre']}: {alumno['calificacion']}")