# reportes.py
from utilidades.utilidades import TARIFAS_FRANJA

def mostrar_informe_emisora(parrilla):
    """Muestra el informe completo de la emisora."""
    if not parrilla:
        print("No hay datos suficientes para generar el informe (la parrilla está vacía).")
        return

    print("\n" + "="*40)
    print("      INFORME GENERAL DE LA EMISORA")
    print("="*40)

    # 1. Minutos al aire por franja
    minutos_por_franja = {"Mañana": 0, "Tarde": 0, "Noche": 0, "Madrugada": 0}
    for datos in parrilla.values():
        franja, _, duracion, _ = datos
        if franja in minutos_por_franja:
            minutos_por_franja[franja] += duracion

    print("\n[1] Minutos al aire por franja:")
    for franja, minutos in minutos_por_franja.items():
        print(f"  • {franja}: {minutos} minutos")

    # 2. El programa que más factura
    max_facturacion = -1
    programa_top = ""
    for nombre, datos in parrilla.items():
        franja, _, _, cunas = datos
        facturacion = len(cunas) * TARIFAS_FRANJA.get(franja, 0)
        if facturacion > max_facturacion:
            max_facturacion = facturacion
            programa_top = nombre

    print(f"\n[2] Programa que más factura:")
    if programa_top:
        print(f"  • {programa_top} (${max_facturacion:,})")
    else:
        print("  • Ninguno")

    # 3. Cuántas cuñas hay en total
    total_cunas = 0
    for datos in parrilla.values():
        total_cunas += len(datos[3])
    print(f"\n[3] Total de cuñas publicitarias pautadas: {total_cunas}")

    # 4. El locutor con más programas
    conteo_locutores = {}
    for datos in parrilla.values():
        locutor = datos[1]
        conteo_locutores[locutor] = conteo_locutores.get(locutor, 0) + 1

    print(f"\n[4] Locutor con más programas:")
    if conteo_locutores:
        locutor_top = max(conteo_locutores, key=conteo_locutores.get)
        print(f"  • {locutor_top} ({conteo_locutores[locutor_top]} programas)")
    else:
        print("  • Ninguno")
    print("="*40)