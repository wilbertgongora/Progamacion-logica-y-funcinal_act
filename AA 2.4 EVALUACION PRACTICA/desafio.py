from functools import reduce

# ----------------------------
# Funciones puras
# ----------------------------

def es_valida(respuesta):
    """Verifica si una respuesta es válida (no vacía ni None)."""
    return respuesta is not None and respuesta != ""

def filtrar_respuestas_validas(respuestas):
    """Filtra respuestas válidas usando filter."""
    return list(filter(es_valida, respuestas))

def mapear_a_puntuaciones(respuestas):
    """Mapea las respuestas textuales a puntuaciones numéricas."""
    escala = {
        "Excelente": 5,
        "Muy bien": 4,
        "Bien": 3,
        "Regular": 2,
        "Mal": 1
    }
    return [escala.get(r, 0) for r in respuestas]

def calcular_promedio(puntuaciones):
    """Calcula el promedio de una lista de puntuaciones usando reduce."""
    if not puntuaciones:
        return 0.0
    suma = reduce(lambda x, y: x + y, puntuaciones)
    return suma / len(puntuaciones)

def contar_elemento_recursivo(lista, elemento):
    """Cuenta cuántas veces aparece un elemento en la lista usando recursividad."""
    if not lista:
        return 0
    return (1 if lista[0] == elemento else 0) + contar_elemento_recursivo(lista[1:], elemento)

# ----------------------------
# Entrada de datos con consola
# ----------------------------

def ejecutar_encuesta():
    preguntas = [
        "¿Qué opinas del curso de Base de Datos?",
        "¿Qué opinas del curso de Programación Web?",
        "¿Qué opinas del curso de Inteligencia Artificial?",
        "¿Qué opinas del curso de Redes?"
    ]

    opciones = ["Excelente", "Muy bien", "Bien", "Regular", "Mal"]
    respuestas = []

    print("📋 Encuesta de Opinión sobre Materias")
    print("Opciones válidas:", ", ".join(opciones), "\n")

    for pregunta in preguntas:
        respuesta = input(f"{pregunta}\n> ").strip()
        respuestas.append(respuesta)

    respuestas_validas = filtrar_respuestas_validas(respuestas)
    puntuaciones = mapear_a_puntuaciones(respuestas_validas)
    promedio = calcular_promedio(puntuaciones)
    excelentes = contar_elemento_recursivo(respuestas_validas, "Excelente")

    print("\n✅ Resultados de la Encuesta:")
    print("Respuestas válidas:", respuestas_validas)
    print("Puntuaciones numéricas:", puntuaciones)
    print(f"Promedio general: {promedio:.2f}")
    print(f"Cantidad de 'Excelente': {excelentes} de {len(preguntas)} materias")

# Ejecutar la encuesta
ejecutar_encuesta()
