# main.py
from pathlib import Path
import sys

ROOT_DIR = str(Path(__file__).resolve().parents[1])
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from utilidades.utilidades import formatear_parrilla
from registro.registro import registrar_programa, sacar_programa, cambiar_locutor
from calculos.calculo import calcular_facturacion_programa, calcular_minutos_ocupados
from busquedas.busqueda import consultar_por_nombre, buscar_por_locutor, listar_por_franja
from reportes.reportes import mostrar_informe_emisora

def main():
    # Estructura principal: Diccionario de la emisora
    # Clave: Nombre del programa | Valor: [franja, locutor, duración, [cuñas]]
    parrilla = {}

    while True:
        print("\n" + "="*45)
        print("        SISTEMA DE GESTIÓN DE EMISORA")
        print("="*45)
        print("1. Registrar un programa nuevo")
        print("2. Retirar (sacar) un programa de la parrilla")
        print("3. Cambiar el locutor de un programa")
        print("4. Calcular facturación por cuñas de un programa")
        print("5. Calcular minutos totales ocupados en la parrilla")
        print("6. Consultar un programa por su nombre")
        print("7. Buscar programas de un locutor")
        print("8. Listar programas por franja horaria")
        print("9. Mostrar informe general de la emisora")
        print("10. Ver toda la parrilla actual")
        print("11. Salir")
        
        opcion = input("\nSeleccione una opción (1-11): ").strip()

        if opcion == "1":
            print("\n--- REGISTRAR PROGRAMA ---")
            registrar_programa(parrilla)
        elif opcion == "2":
            print("\n--- RETIRAR PROGRAMA ---")
            sacar_programa(parrilla)
        elif opcion == "3":
            print("\n--- CAMBIAR LOCUTOR ---")
            cambiar_locutor(parrilla)
        elif opcion == "4":
            print("\n--- CALCULAR FACTURACIÓN ---")
            calcular_facturacion_programa(parrilla)
        elif opcion == "5":
            print("\n--- MINUTOS OCUPADOS ---")
            calcular_minutos_ocupados(parrilla)
        elif opcion == "6":
            print("\n--- CONSULTAR POR NOMBRE ---")
            consultar_por_nombre(parrilla)
        elif opcion == "7":
            print("\n--- BUSCAR POR LOCUTOR ---")
            buscar_por_locutor(parrilla)
        elif opcion == "8":
            print("\n--- LISTAR POR FRANJA ---")
            listar_por_franja(parrilla)
        elif opcion == "9":
            print("\n--- INFORME GENERAL ---")
            mostrar_informe_emisora(parrilla)
        elif opcion == "10":
            print(formatear_parrilla(parrilla))
        elif opcion == "11":
            print("\n¡Gracias por usar el sistema de la emisora. Hasta pronto!")
            break
        else:
            print("\nOpción no válida. Por favor, ingrese un número del 1 al 11.")

if __name__ == "__main__":
    main()