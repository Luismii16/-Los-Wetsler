# utilidades.py

# Constantes de tarifas por minuto de cuña según la franja horaria
TARIFAS_FRANJA = {
    "Mañana": 5000,
    "Tarde": 4000,
    "Noche": 3000,
    "Madrugada": 2000
}

FRANJAMAS_VALIDAS = ["Mañana", "Tarde", "Noche", "Madrugada"]

def validar_franja(franja):
    """Valida que la franja ingresada exista en las definidas."""
    return franja in FRANJAMAS_VALIDAS

def validar_duracion(duracion):
    """Valida que la duración en minutos sea un número positivo."""
    try:
        val = int(duracion)
        return val > 0
    except ValueError:
        return False

def formatear_parrilla(parrilla):
    """Arma el texto ordenado con el que se imprime la parrilla en pantalla."""
    if not parrilla:
        return "La parrilla de la emisora está vacía."
    
    texto = "\n" + "="*50 + "\n"
    texto += "          PARRILLA DE PROGRAMACIÓN - EMISORA\n"
    texto += "="*50 + "\n"
    for programa, datos in parrilla.items():
        franja, locutor, duracion, cunas = datos
        texto += f"• Programa: {programa}\n"
        texto += f"  - Franja horaria: {franja}\n"
        texto += f"  - Locutor: {locutor}\n"
        texto += f"  - Duración: {duracion} minutos\n"
        texto += f"  - Cuñas publicitarias: {len(cunas)} pautadas ({', '.join(cunas) if cunas else 'Ninguna'})\n"
        texto += "-" * 50 + "\n"
    return texto