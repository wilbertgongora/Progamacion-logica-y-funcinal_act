jugadores =[
{"nombre":"brandon", "edad":22},
{"nombre":"javier", "edad":30},
{"nombre":"carlos", "edad":18},
{"nombre":"jorge", "edad":25}
]

nombres_jugadores =list(map(lambda jugador: jugador["nombre"], jugadores))
print(nombres_jugadores)