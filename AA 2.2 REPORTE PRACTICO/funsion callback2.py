# Callback para Registro de Actividades en Cursos

# Función de orden superior que recibe un callback
def registrar_evento(evento, callback):
    callback(evento)  # Llama al callback con el evento

# Callback que imprime un registro de actividad
def registrar_curso(mensaje):
    print(f"📝 Registro: {mensaje}")

# Llamar a la función con el callback
registrar_evento("El usuario completó el módulo 1 de programacion", registrar_curso)
registrar_evento("Nueva tarea disponible en el curso de Python impartido por wilbert gongora", registrar_curso)
