import random

frases = [
    'No persigas la felicidad, créala.',
    'Todas las cosas son difíciles antes de ser fáciles.',
    'El pájaro madrugador atrapa el gusano, pero el segundo ratón obtiene el queso.',
    'Si comes algo y nadie te ve comerlo, no tiene calorías.',
    'Alguien en tu vida necesita una carta tuya.',
    '¡No solo pienses. Actúa!',
    'Tu corazón se saltará un latido.',
    'La fortuna que buscas está en otra galleta.'
]

def fortuna():
    abrir_galleta = random.randint(0, len(frases) - 1)
    print(frases[abrir_galleta])

# Llamar a la función para obtener una frase aleatoria
fortuna()