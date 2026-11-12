# registro.py
from utilidades.utilidades import validar_franja, validar_duracion

def registrar_programa(parrilla):
    """Registra un programa nuevo validando que el nombre no exista."""
    nombre = input("Ingrese el nombre del programa: ").strip().capitalize()
    
    if nombre in parrilla:
        print(f"Error: El programa '{nombre}' ya existe en la parrilla.")
        return

    franja = input(f"Ingrese la franja horaria (Mañana, Tarde, Noche, Madrugada): ").strip().capitalize()
    if not validar_franja(franja):
        print("Error: Franja horaria no válida.")
        return

    locutor = input("Ingrese el nombre del locutor: ").strip().title()

    duracion_str = input("Ingrese la duración en minutos: ").strip()
    if not validar_duracion(duracion_str):
        print("Error: La duración debe ser un número entero mayor a 0.")
        return
    duracion = int(duracion_str)

    cunas_input = input("Ingrese las cuñas publicitarias separadas por coma (o presione Enter si no tiene): ")
    cunas = [c.strip() for c in cunas_input.split(",")] if cunas_input else []

    # Guardar en el diccionario principal
    parrilla[nombre] = [franja, locutor, duracion, cunas]
    print(f"¡Programa '{nombre}' registrado con éxito!")

def sacar_programa(parrilla):
    """Saca (elimina) un programa de la parrilla."""
    nombre = input("Ingrese el nombre del programa que desea retirar de la parrilla: ").strip().capitalize()
    if nombre in parrilla:
        del parrilla[nombre]
        print(f"El programa '{nombre}' ha sido retirado de la parrilla.")
    else:
        print(f"No se encontró un programa con el nombre '{nombre}'.")

def cambiar_locutor(parrilla):
    """Cambia el locutor a un programa ya registrado."""
    nombre = input("Ingrese el nombre del programa al que desea cambiarle el locutor: ").strip().capitalize()
    if nombre in parrilla:
        nuevo_locutor = input("Ingrese el nombre del nuevo locutor: ").strip().title()
        # parrilla[nombre] es una lista: [franja, locutor, duracion, cunas]
        parrilla[nombre][1] = nuevo_locutor
        print(f"¡Locutor actualizado con éxito para el programa '{nombre}'!")
    else:
        print(f"El programa '{nombre}' no está registrado.")