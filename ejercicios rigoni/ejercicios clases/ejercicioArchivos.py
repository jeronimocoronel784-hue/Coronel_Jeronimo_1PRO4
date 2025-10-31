import csv
import os

ARCHIVO = "productos.csv"

# -------------------- Funciones --------------------

def inicializar_archivo():
    """Crea el archivo CSV con encabezados si no existe."""
    if not os.path.exists(ARCHIVO):
        with open(ARCHIVO, "w", newline="", encoding="utf-8") as f:
            escritor = csv.DictWriter(f, fieldnames=["nombre", "precio"])
            escritor.writeheader()

def leer_productos():
    """Lee los productos del archivo CSV y devuelve una lista de diccionarios."""
    productos = []
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            for fila in lector:
                productos.append({"nombre": fila["nombre"], "precio": float(fila["precio"])})
    except FileNotFoundError:
        inicializar_archivo()
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
    return productos

def mostrar_productos():
    """Muestra todos los productos con el total de precios."""
    productos = leer_productos()
    if not productos:
        print("\nNo hay productos registrados.\n")
        return

    print("\nProductos registrados:\n")
    total = 0
    for p in productos:
        print(f"- {p['nombre']} → ${p['precio']:.2f}")
        total += p['precio']
    print(f"\nTotal de precios: ${total:.2f}\n")

def agregar_producto():
    """Agrega un nuevo producto validando nombre único y precio positivo."""
    nombre = input("Ingrese el nombre del producto: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
        return

    # Leer productos existentes
    productos = leer_productos()

    # Validar que no exista otro producto con el mismo nombre (sin distinguir mayúsculas/minúsculas)
    for p in productos:
        if p["nombre"].lower() == nombre.lower():
            print("Ya existe un producto con ese nombre. No se puede agregar duplicado.\n")
            return

    # Validar precio numérico y positivo
    try:
        precio = float(input("Ingrese el precio: "))
        if precio <= 0:
            raise ValueError
    except ValueError:
        print("El precio debe ser un número positivo.")
        return

    # Si pasa las validaciones, agregar el producto
    with open(ARCHIVO, "a", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=["nombre", "precio"])
        escritor.writerow({"nombre": nombre, "precio": precio})

    print("Producto agregado correctamente.\n")

def eliminar_producto():
    """Elimina un producto existente si se encuentra en el archivo."""
    nombre = input("Ingrese el nombre del producto a eliminar: ").strip()
    productos = leer_productos()

    encontrado = False
    nuevos_productos = []
    for p in productos:
        if p["nombre"].lower() != nombre.lower():
            nuevos_productos.append(p)
        else:
            encontrado = True

    if not encontrado:
        print("Producto no encontrado.\n")
        return

    with open(ARCHIVO, "w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=["nombre", "precio"])
        escritor.writeheader()
        escritor.writerows(nuevos_productos)

    print("Producto eliminado correctamente.\n")

def actualizar_precio():
    """Actualiza el precio de un producto existente."""
    nombre = input("Ingrese el nombre del producto a actualizar: ").strip()
    productos = leer_productos()
    encontrado = False

    for p in productos:
        if p["nombre"].lower() == nombre.lower():
            try:
                nuevo_precio = float(input("Ingrese el nuevo precio: "))
                if nuevo_precio <= 0:
                    raise ValueError
                p["precio"] = nuevo_precio
                encontrado = True
            except ValueError:
                print("El precio debe ser un número positivo.")
            break

    if not encontrado:
        print("Producto no encontrado.\n")
        return

    with open(ARCHIVO, "w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=["nombre", "precio"])
        escritor.writeheader()
        escritor.writerows(productos)

    print("Precio actualizado correctamente.\n")

# -------------------- Programa Principal --------------------

def menu():
    """Muestra el menú principal y controla la ejecución."""
    inicializar_archivo()

    while True:
        print("====== MENÚ DE PRODUCTOS ======")
        print("1. Mostrar productos")
        print("2. Agregar producto")
        print("3. Eliminar producto")
        print("4. Salir")
        print("5. Actualizar precio de un producto")
        print("===============================")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            mostrar_productos()
        elif opcion == "2":
            agregar_producto()
        elif opcion == "3":
            eliminar_producto()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        elif opcion == "5":
            actualizar_precio()
        else:
            print("Opción no válida. Intente nuevamente.\n")

# -------------------- Ejecución --------------------
if __name__ == "__main__":
    menu()

