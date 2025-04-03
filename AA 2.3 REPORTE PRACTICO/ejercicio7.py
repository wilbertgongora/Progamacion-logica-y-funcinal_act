jugadores =[
{"nombre":"brandon", "edad":22},
{"nombre":"javier", "edad":30},
{"nombre":"carlos", "edad":18},
{"nombre":"jorge", "edad":25}
]

jugadores_mayores =list(filter(lambda jugador: jugador ["edad"] >23, jugadores ))

print(jugadores_mayores)