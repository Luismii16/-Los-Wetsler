# busquedas.py

def consultar_por_nombre(parrilla):
    """Consulta un programa por su nombre y muestra su información detallada."""
    nombre = input("Ingrese el nombre del programa a buscar: ").strip().capitalize()
    if nombre in parrilla:
        franja, locutor, duracion, cunas = parrilla[nombre]
        print(f"\n--- Programa Encontrado ---")
        print(f"Nombre: {nombre}")
        print(f"Franja: {franja}")
        print(f"Locutor: {locutor}")
        print(f"Duración: {duracion} minutos")
        print(f"Cuñas: {', '.join(cunas) if cunas else 'Ninguna'}")
    else:
        print(f"No se encontró ningún programa llamado '{nombre}'.")

def buscar_por_locutor(parrilla):
    """Busca y lista todos los programas de un locutor específico."""
    locutor_buscado = input("Ingrese el nombre del locutor: ").strip().title()
    encontrados = []

    for nombre, datos in parrilla.items():
        if datos[1] == locutor_buscado:
            encontrados.append(nombre)

    if encontrados:
        print(f"\nProgramas del locutor '{locutor_buscado}':")
        for prog in encontrados:
            print(f"- {prog}")
    else:
        print(f"El locutor '{locutor_buscado}' no tiene programas registrados.")

def listar_por_franja(parrilla):
    """Lista los programas de una franja horaria determinada."""
    franja_buscada = input("Ingrese la franja horaria a consultar (Mañana, Tarde, Noche, Madrugada): ").strip().capitalize()
    encontrados = []

    for nombre, datos in parrilla.items():
        if datos[0] == franja_buscada:
            encontrados.append(nombre)

    if encontrados:
        print(f"\nProgramas en la franja '{franja_buscada}':")
        for prog in encontrados:
            print(f"- {prog}")
    else:
        print(f"No hay programas en la franja '{franja_buscada}'.")