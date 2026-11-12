# calculos.py
from utilidades.utilidades import TARIFAS_FRANJA

def calcular_facturacion_programa(parrilla):
    """Calcula lo que factura un programa por sus cuñas según la tarifa de su franja."""
    nombre = input("Ingrese el nombre del programa a calcular: ").strip().capitalize()
    if nombre not in parrilla:
        print(f"El programa '{nombre}' no existe.")
        return

    franja, _, _, cunas = parrilla[nombre]
    tarifa_por_cuna = TARIFAS_FRANJA.get(franja, 0)
    total_facturado = len(cunas) * tarifa_por_cuna

    print(f"\n--- Facturación para '{nombre}' ---")
    print(f"Franja: {franja} (Tarifa por cuña: ${tarifa_por_cuna:,})")
    print(f"Cantidad de cuñas: {len(cunas)}")
    print(f"Total a facturar: ${total_facturado:,}")

def calcular_minutos_ocupados(parrilla):
    """Calcula cuántos minutos de la parrilla están ocupados en total."""
    total_minutos = 0
    for datos in parrilla.values():
        duracion = datos[2]
        total_minutos += duracion
    
    print(f"\nMinutos totales ocupados en la parrilla: {total_minutos} minutos.")
    return total_minutos