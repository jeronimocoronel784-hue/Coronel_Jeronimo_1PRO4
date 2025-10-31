# Ejercicio: Búsqueda recursiva de la salida en un laberinto

# LEYENDA:
# P = Pared
#   = Camino
# S = Salida
# D = Dragón (posición inicial)

# Representación del laberinto como lista de listas (matriz)
laberinto = [
    ["P", "P", "P", "P", "P"],
    ["P", "D", " ", " ", "P"],
    ["P", " ", "P", " ", "S"],
    ["P", " ", " ", " ", "P"],
    ["P", "P", "P", "P", "P"]
]

def imprimir_laberinto(lab):
    """Imprime el laberinto de forma legible."""
    for fila in lab:
        print(" ".join(fila))
    print()  # Línea en blanco para separar visualmente

def buscar_salida(laberinto, fila, columna, pasos=0):
    """
    Función recursiva que busca la salida en el laberinto.
    Parámetros:
    - laberinto: matriz que representa el laberinto.
    - fila, columna: posición actual del dragón.
    - pasos: cantidad de movimientos realizados (para el desafío extra).
    """
    # Verificar que la posición esté dentro de los límites
    if fila < 0 or fila >= len(laberinto) or columna < 0 or columna >= len(laberinto[0]):
        return False

    # Si llegamos a una pared o una celda ya visitada, no seguimos
    if laberinto[fila][columna] in ("P", "."):
        return False

    # Si llegamos a la salida, mostramos el laberinto y devolvemos True
    if laberinto[fila][columna] == "S":
        print(f"¡El dragón encontró la salida en {pasos} pasos!\n")
        imprimir_laberinto(laberinto)
        return True

    # Marcar la posición actual como visitada
    if laberinto[fila][columna] != "D":  # No sobreescribimos la posición inicial del dragón
        laberinto[fila][columna] = "."

    # Probar moverse en las 4 direcciones: arriba, abajo, izquierda, derecha
    if (buscar_salida(laberinto, fila - 1, columna, pasos + 1) or  # Arriba
        buscar_salida(laberinto, fila + 1, columna, pasos + 1) or  # Abajo
        buscar_salida(laberinto, fila, columna - 1, pasos + 1) or  # Izquierda
        buscar_salida(laberinto, fila, columna + 1, pasos + 1)):   # Derecha
        return True

    # Si ninguna dirección lleva a la salida, retrocedemos
    laberinto[fila][columna] = " "  # Desmarcamos la celda (backtracking)
    return False

# Buscar la posición inicial del dragón (D)
posicion_dragon = None
for i in range(len(laberinto)):
    for j in range(len(laberinto[i])):
        if laberinto[i][j] == "D":
            posicion_dragon = (i, j)
            break

# Mostrar laberinto inicial
print("Laberinto inicial:")
imprimir_laberinto(laberinto)

# Iniciar la búsqueda desde la posición del dragón
if posicion_dragon:
    exito = buscar_salida(laberinto, posicion_dragon[0], posicion_dragon[1])
    if not exito:
        print("No se encontró ninguna salida posible.")
else:
    print("No se encontró la posición inicial del dragón (D).")
