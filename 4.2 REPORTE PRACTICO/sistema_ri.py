class SistemaRiegoInteligente:
    def __init__(self):
        # Datos del sistema (podrían venir de sensores en una implementación real)
        self.parametros = {
            'humedad_suelo': 'baja',
            'temperatura': 35,
            'hora': 14,
            'probabilidad_lluvia': False,
            'viento': 'flojo',
            'nivel_tanque': 'suficiente',
            'nivel_fertilizante': 'adecuado'
        }
        
        # Ejecutar análisis automáticamente al iniciar
        self.analizar_sistema()

    def evaluar_condiciones_riego(self):
        """Evalúa si se cumplen las condiciones para el riego"""
        condiciones = {
            'Humedad del suelo es baja': self.parametros['humedad_suelo'] == 'baja',
            'No hay probabilidad de lluvia': not self.parametros['probabilidad_lluvia'],
            'Hora adecuada (antes de 10 o después de 18)': self.parametros['hora'] < 10 or self.parametros['hora'] > 18,
            'Viento es flojo o moderado': self.parametros['viento'] in ['flojo', 'moderado'],
            'Tanque tiene suficiente agua': self.parametros['nivel_tanque'] == 'suficiente'
        }
        return condiciones

    def verificar_alertas(self):
        """Identifica condiciones que requieren atención especial"""
        alertas = []
        if self.parametros['temperatura'] > 30:
            alertas.append(f"Temperatura alta ({self.parametros['temperatura']}°C)")
        if self.parametros['viento'] == 'fuerte':
            alertas.append("Viento fuerte puede afectar el riego")
        if self.parametros['nivel_tanque'] == 'bajo':
            alertas.append("Nivel de agua en tanque bajo")
        if self.parametros['nivel_fertilizante'] == 'bajo':
            alertas.append("Nivel de fertilizante bajo")
        return alertas

    def generar_recomendacion(self, condiciones, alertas):
        """Genera recomendaciones basadas en el análisis"""
        riego_recomendado = all(condiciones.values())
        
        if not riego_recomendado:
            return "No se recomienda activar el riego en las condiciones actuales."
        
        if not alertas:
            return "Se recomienda activar el riego. Condiciones óptimas."
        
        recomendacion = "Se recomienda activar el riego con consideraciones:\n"
        for alerta in alertas:
            if "Temperatura" in alerta:
                recomendacion += "- Programar riego en horas más frescas\n"
            elif "Viento" in alerta:
                recomendacion += "- Ajustar aspersores para minimizar deriva\n"
            elif "agua" in alerta:
                recomendacion += "- Monitorear nivel de agua durante el riego\n"
            elif "fertilizante" in alerta:
                recomendacion += "- Verificar niveles de fertilizante\n"
        
        return recomendacion

    def analizar_sistema(self):
        """Realiza el análisis completo del sistema"""
        # Obtener condiciones y alertas
        condiciones = self.evaluar_condiciones_riego()
        alertas = self.verificar_alertas()
        recomendacion = self.generar_recomendacion(condiciones, alertas)
        
        # Mostrar reporte completo
        print("\n=== INFORME DEL SISTEMA DE RIEGO ===")
        print("\n[Parámetros actuales]")
        for param, valor in self.parametros.items():
            print(f"- {param.replace('_', ' ').title()}: {valor}")
        
        print("\n[Evaluación de condiciones para riego]")
        for cond, cumple in condiciones.items():
            estado = "Cumple" if cumple else "No cumple"
            print(f"- {cond}: {estado}")
        
        print(f"\n[Conclusión]: {'Condiciones adecuadas para riego' if all(condiciones.values()) else 'Condiciones no adecuadas para riego'}")
        
        if alertas:
            print("\n[Alertas activas]")
            for alerta in alertas:
                print(f"- {alerta}")
        
        print("\n[Recomendación]")
        print(recomendacion)
        
        print("\n[Estado de fertilización]")
        estado_fert = "Disponible (nivel adecuado)" if self.parametros['nivel_fertilizante'] == 'adecuado' else "No disponible (nivel bajo)"
        print(f"- Fertilización: {estado_fert}")

        print("\n=== FIN DEL INFORME ===\n")

# Ejecutar el sistema automáticamente
if __name__ == "__main__":
    print("Iniciando análisis del sistema de riego...\n")
    sistema = SistemaRiegoInteligente()