% --- Base de hechos ---
humedad_suelo(baja).
temperatura(35).
hora(20).
probabilidad_lluvia(false).
viento(flojo).
nivel_tanque(suficiente).
nivel_fertilizante(adecuado).

% --- Reglas para condiciones ---
hora_adecuada :- hora(H), (H < 10 ; H > 18).
viento_apto :- viento(flojo) ; viento(moderado).
tanque_con_agua :- nivel_tanque(suficiente).
fertilizante_ok :- nivel_fertilizante(adecuado).

% --- Activación del riego ---
activar_riego :-
    humedad_suelo(baja),
    probabilidad_lluvia(false),
    hora_adecuada,
    viento_apto,
    tanque_con_agua.

% --- Estado del sistema ---
estado_riego('Activado') :- activar_riego.
estado_riego('No activado') :- \+ activar_riego.

% --- Alertas ---
alerta_calor :- temperatura(T), T >= 32.
alerta_viento :- viento(fuerte).
alerta_tanque :- nivel_tanque(bajo).
alerta_fertilizante :- nivel_fertilizante(bajo).

% --- Recomendaciones ---
recomendacion :-
    activar_riego,
    alerta_calor,
    !,
    writeln('Alerta: Riego activado con temperatura alta. Considere riego más corto o en horas más frescas.').

recomendacion :-
    activar_riego,
    alerta_viento,
    !,
    writeln('Alerta: Hay viento fuerte. El riego puede no ser efectivo.').

recomendacion :-
    activar_riego,
    alerta_tanque,
    !,
    writeln('Alerta: Nivel del tanque bajo. Podría quedarse sin agua.').

recomendacion :-
    activar_riego,
    alerta_fertilizante,
    !,
    writeln('Alerta: Fertilizante bajo. Considere reponer el fertilizante.').

recomendacion :-
    \+ activar_riego,
    !,
    writeln('Riego no activado. Verifique condiciones: humedad, hora, viento, tanque.').

recomendacion :-
    writeln('Riego activado. Todas las condiciones son óptimas.').

% --- Servicio extra: fertilización ---
fertilizar :- 
    fertilizante_ok,
    writeln('Fertilización activada. Nivel de fertilizante adecuado.').

fertilizar :-
    \+ fertilizante_ok,
    writeln('No se puede fertilizar. Nivel de fertilizante bajo.').

% --- Estado general del sistema ---
estado_general :-
    estado_riego(Estado), writeln(['Estado de riego:', Estado]),
    (alerta_calor -> writeln('Alerta: Temperatura alta'); true),
    (alerta_viento -> writeln('Alerta: Viento fuerte'); true),
    (alerta_tanque -> writeln('Alerta: Tanque bajo'); true),
    (alerta_fertilizante -> writeln('Alerta: Fertilizante bajo'); true),
    (activar_riego -> writeln('Sistema de riego activo'); writeln('Sistema de riego inactivo')).
