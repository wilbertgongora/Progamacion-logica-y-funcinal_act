def filtrar_tareas(tareas, condicion):
    return [tarea for tarea in tareas if condicion(tarea)]


tareas = [
    ("Estudiar para el examen de redes", True),
    ("Hacer proyecto de bases de datos", False),
    ("Preparar presentación de sistemas operativos", True)
]


tareas_completadas = filtrar_tareas(tareas, lambda x: x[1])
print("Tareas completadas:", tareas_completadas)

tareas_pendientes = filtrar_tareas(tareas, lambda x: not x[1])
print("Tareas pendientes:", tareas_pendientes)