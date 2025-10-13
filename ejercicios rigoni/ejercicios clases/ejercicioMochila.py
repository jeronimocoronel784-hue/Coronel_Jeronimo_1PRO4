

def crear_mochila():
    """Crea la mochila pidiendo al usuario la cantidad de espacios."""
    while True:
        try:
            tamaño = int(input("Ingresa cuántos espacios tendrá la mochila: "))
            if tamaño <= 0:
                print("Error: el número debe ser mayor que cero.")
            else:
                # Devuelve una lista vacía con esa cantidad de espacios
                return ["--- vacío ---"] * tamaño
        except ValueError:
            print("Error: debes ingresar un número entero válido.")


def mostrar_menu():
    """Muestra el menú principal."""
    print("\n--- Menú de la Mochila ---")
    print("1. Guardar objeto")
    print("2. Ver mochila")
    print("3. Eliminar objeto")
    print("4. Salir")


def guardar_objeto(mochila):
    """Permite guardar un objeto mágico en una posición específica."""
    try:
        pos = int(input(f"Ingrese la posición (0-{len(mochila)-1}): "))
        objeto = input("Ingresa el objeto mágico: ").strip()

        if objeto == "":
            print("Error: el nombre del objeto no puede estar vacío.")
            return

        mochila[pos] = objeto
        print(f"'{objeto}' guardado en el espacio {pos}.")

    except ValueError:
        print("Error: debes ingresar un número válido para la posición.")
    except IndexError:
        print("Error: esa posición no existe en la mochila.")


def ver_mochila(mochila):
    """Muestra el contenido de la mochila."""
    print("\nContenido de la mochila:")
    for i, objeto in enumerate(mochila):
        print(f"Espacio {i}: {objeto}")


def eliminar_objeto(mochila):
    """Permite eliminar un objeto (deja el espacio vacío)."""
    try:
        pos = int(input(f"Ingrese la posición a eliminar (0-{len(mochila)-1}): "))

        if mochila[pos] == "--- vacío ---":
            print("Ese espacio ya está vacío.")
        else:
            print(f"Objeto '{mochila[pos]}' eliminado del espacio {pos}.")
            mochila[pos] = "--- vacío ---"

    except ValueError:
        print("Error: debes ingresar un número válido para la posición.")
    except IndexError:
        print("Error: esa posición no existe en la mochila.")


# ---------------------------------------------------------
# Programa principal
# ---------------------------------------------------------
def main():
    mochila = crear_mochila()

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            guardar_objeto(mochila)
        elif opcion == "2":
            ver_mochila(mochila)
        elif opcion == "3":
            eliminar_objeto(mochila)
        elif opcion == "4":
            print("Hasta la próxima, aventurero.")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")


# Ejecutar el programa
if __name__ == "__main__":
    main()