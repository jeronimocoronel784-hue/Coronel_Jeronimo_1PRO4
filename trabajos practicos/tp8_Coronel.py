

# Función para crear el archivo inicial (si no existe)

def crear_archivo_inicial():
    try:
        with open("productos.txt", "x", encoding="utf-8") as archivo:
            archivo.write("Lapicera,120.5\n")
            archivo.write("Cuaderno,450.0\n")
            archivo.write("Regla,90.0\n")
            print("Archivo 'productos.txt' creado con productos iniciales.")
    except FileExistsError:
        print("El archivo 'productos.txt' ya existe.")



# Función para leer el archivo y devolver una lista de diccionarios

def leer_productos():
    productos = []
    with open("productos.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            partes = linea.strip().split(",")
            if len(partes) == 3:
                nombre, precio, cantidad = partes
                productos.append({
                    "nombre": nombre,
                    "precio": float(precio),
                    "cantidad": int(cantidad)
                })
    return productos



# Función para mostrar productos en formato legible

def mostrar_productos(productos):
    print("\nListado de productos:")
    for p in productos:
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")



# Función para agregar un nuevo producto desde teclado

def agregar_producto():
    nombre = input("\nIngrese el nombre del producto: ").strip()
    precio = float(input("Ingrese el precio: "))
    cantidad = int(input("Ingrese la cantidad: "))
    # Modo "a" agrega al final del archivo sin borrar el contenido
    with open("productos.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{nombre},{precio},{cantidad}\n")
    print("Producto agregado correctamente.")



# Función para buscar un producto por nombre dentro de la lista

def buscar_producto(productos):
    nombre_buscar = input("\nIngrese el nombre del producto a buscar: ").strip().lower()
    encontrado = False
    for p in productos:
        if p["nombre"].lower() == nombre_buscar:
            print(f"Producto encontrado -> Nombre: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
            encontrado = True
            break
    if not encontrado:
        print("El producto no se encuentra en la lista.")



# Función para guardar todos los productos actualizados en el archivo

def guardar_productos(productos):
    with open("productos.txt", "w", encoding="utf-8") as archivo:
        for p in productos:
            archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")
    print("Archivo actualizado con todos los productos.")



# Función principal que coordina el flujo del programa

def main():
    crear_archivo_inicial()
    productos = leer_productos()
    mostrar_productos(productos)

    opcion = input("\n¿Desea agregar un nuevo producto? (s/n): ").lower()
    if opcion == "s":
        agregar_producto()

    productos = leer_productos()  # Actualizamos la lista
    buscar_producto(productos)

    guardar_productos(productos)
    print("\nPrograma finalizado correctamente.")



# Ejecución del programa

if __name__ == "__main__":
    main()
