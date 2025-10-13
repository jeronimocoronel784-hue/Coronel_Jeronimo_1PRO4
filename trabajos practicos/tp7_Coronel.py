
import json

# Punto 1 y 2: diccionario precios_frutas

def ejercicios_frutas():

    # Punto 1: diccionario inicial
    precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

    # Agregar nuevas frutas 
    precios_frutas['Naranja'] = 1200
    precios_frutas['Manzana'] = 1500
    precios_frutas['Pera'] = 2300

    # Punto 2: actualizar precios 
    precios_frutas['Banana'] = 1330
    precios_frutas['Manzana'] = 1700
    precios_frutas['Melón'] = 2800

    # Punto 3: lista con solo nombres (sin precios)
    lista_frutas = list(precios_frutas.keys())

    # Mostrar resultados
    print("\n--- Punto 1-3: Precios de frutas ---")
    print("Diccionario final de precios:", precios_frutas)
    print("Lista de frutas (solo nombres):", lista_frutas)

    return precios_frutas, lista_frutas

# Punto 4: agenda de 5 contactos (nombre -> número)

def agenda_contactos():

    contactos = {}
    print("\n--- Punto 4: Cargar 5 contactos ---")
    for i in range(1, 6):
        while True:
            nombre = input(f"Ingrese el nombre del contacto #{i}: ").strip()
            if nombre == "":
                print("Nombre no puede estar vacío. Intente nuevamente.")
                continue
            if nombre in contactos:
                print("Ese nombre ya fue ingresado. Ingrese otro nombre.")
                continue
            numero = input(f"Ingrese el número de {nombre}: ").strip()
            if numero == "":
                print("Número no puede estar vacío. Intente nuevamente.")
                continue
            contactos[nombre] = numero
            break

    # Consulta
    nombre_consulta = input("Ingrese un nombre para consultar su número: ").strip()
    numero_encontrado = contactos.get(nombre_consulta)
    if numero_encontrado is not None:
        print(f"Número de {nombre_consulta}: {numero_encontrado}")
    else:
        print(f"No existe un contacto con el nombre '{nombre_consulta}'.")

    return contactos

# Punto 5: frase -> palabras únicas (set) y diccionario de frecuencias

def analizar_frase():

    print("\n--- Punto 5: Análisis de frase ---")
    frase = input("Ingrese una frase: ").strip()
    if frase == "":
        print("Frase vacía. Se considera como ninguna palabra.")
        return set(), {}

    # Normalizamos a minúsculas para contar sin distinción
    palabras = frase.lower().split()
    conjunto_unico = set(palabras)

    # Contar frecuencias
    frecuencias = {}
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

    print("Palabras únicas (set):", conjunto_unico)
    print("Frecuencia por palabra (diccionario):", frecuencias)
    return conjunto_unico, frecuencias

# Punto 6: 3 alumnos, cada uno tupla de 3 notas -> promedio por alumno

def notas_alumnos():

    print("\n--- Punto 6: Alumnos y promedios ---")
    alumnos = {}
    for i in range(1, 4):
        while True:
            nombre = input(f"Ingrese el nombre del alumno #{i}: ").strip()
            if nombre == "":
                print("Nombre no puede ser vacío. Intente nuevamente.")
                continue
            if nombre in alumnos:
                print("Ese nombre ya fue ingresado. Use otro nombre.")
                continue
            break

        notas = []
        for j in range(1, 4):
            while True:
                entrada = input(f"Ingrese la nota {j} de {nombre} (número): ").strip()
                try:
                    nota = float(entrada)
                    if nota < 0:
                        print("La nota no puede ser negativa. Intente nuevamente.")
                        continue
                    notas.append(nota)
                    break
                except ValueError:
                    print("Entrada inválida. Ingrese un número válido.")
        alumnos[nombre] = tuple(notas)

    # Calcular y mostrar promedios
    promedios = {}
    for nombre, tupla_notas in alumnos.items():
        promedio = sum(tupla_notas) / len(tupla_notas)
        promedios[nombre] = promedio
        print(f"Promedio de {nombre}: {promedio:.2f}")

    return alumnos, promedios

# Punto 7: sets de aprobados Parcial 1 y Parcial 2 -> intersección, simétrico, unión

def procesar_aprobados():

    print("\n--- Punto 7: Aprobados en parciales (ejemplo) ---")
    # Ejemplo de sets; el enunciado no exige entrada, por lo que se usan sets de ejemplo.
    parcial1 = {"Ana", "Luis", "Marta", "Diego"}
    parcial2 = {"Marta", "Diego", "Carlos", "Sofia"}

    ambos = parcial1.intersection(parcial2)            # aprobaron ambos
    solo_uno = parcial1.symmetric_difference(parcial2) # aprobaron solo uno
    al_menos_uno = parcial1.union(parcial2)            # aprobaron al menos uno

    print("Parcial 1:", parcial1)
    print("Parcial 2:", parcial2)
    print("Aprobaron ambos parciales:", ambos)
    print("Aprobaron solo uno de los dos parciales:", solo_uno)
    print("Aprobaron al menos un parcial (sin repetir):", al_menos_uno)

    return parcial1, parcial2, ambos, solo_uno, al_menos_uno

# Punto 8: diccionario productos->stock con operaciones de consulta/agregado

def gestionar_stock():

    print("\n--- Punto 8: Gestión de stock ---")
    stock = {
        "Arroz": 50,
        "Fideos": 30,
        "Leche": 20
    }

    print("Stock inicial:", stock)
    producto = input("Ingrese el nombre del producto a consultar/modificar: ").strip()
    if producto == "":
        print("Nombre de producto vacío. Operación cancelada.")
        return stock

    if producto in stock:
        print(f"Stock actual de {producto}: {stock[producto]}")
        # Preguntar si quiere agregar unidades
        while True:
            respuesta = input("¿Desea agregar unidades a este producto? (s/n): ").strip().lower()
            if respuesta in ("s", "si"):
                while True:
                    cantidad_str = input("Ingrese la cantidad a agregar (entero positivo): ").strip()
                    try:
                        cantidad = int(cantidad_str)
                        if cantidad <= 0:
                            print("La cantidad debe ser mayor que cero.")
                            continue
                        stock[producto] += cantidad
                        print(f"Nuevo stock de {producto}: {stock[producto]}")
                        break
                    except ValueError:
                        print("Entrada inválida. Ingrese un entero.")
                break
            elif respuesta in ("n", "no"):
                print("No se realizaron cambios en el stock.")
                break
            else:
                print("Respuesta no válida. Responda 's' o 'n'.")
    else:
        # Producto no existe: ofrecer agregar nuevo producto
        while True:
            respuesta = input(f"El producto '{producto}' no existe. ¿Desea agregarlo? (s/n): ").strip().lower()
            if respuesta in ("s", "si"):
                while True:
                    cantidad_str = input("Ingrese la cantidad inicial (entero >= 0): ").strip()
                    try:
                        cantidad = int(cantidad_str)
                        if cantidad < 0:
                            print("La cantidad no puede ser negativa.")
                            continue
                        stock[producto] = cantidad
                        print(f"Producto '{producto}' agregado con stock {cantidad}.")
                        break
                    except ValueError:
                        print("Entrada inválida. Ingrese un entero.")
                break
            elif respuesta in ("n", "no"):
                print("No se agregó el producto.")
                break
            else:
                print("Respuesta no válida. Responda 's' o 'n'.")

    print("Stock final:", stock)
    return stock

# Punto 9: agenda con claves (día, hora) -> evento; permitir consultar por día y hora

def agenda_eventos():

    print("\n--- Punto 9: Agenda (día, hora) -> evento ---")
    # Ejemplo de agenda con algunas entradas
    agenda = {
        ("Lunes", "09:00"): "Clase de Programación",
        ("Lunes", "11:00"): "Reunión de equipo",
        ("Martes", "14:00"): "Entrega TP",
        ("Miércoles", "16:00"): "Tutoria"
    }

    print("Agenda de ejemplo cargada.")
    dia = input("Ingrese el día a consultar (ej: Lunes): ").strip()
    hora = input("Ingrese la hora a consultar (formato HH:MM, ej: 09:00): ").strip()
    if dia == "" or hora == "":
        print("Día u hora vacíos. Consulta cancelada.")
        return agenda

    evento = agenda.get((dia, hora))
    if evento is not None:
        print(f"En {dia} a las {hora} hay: {evento}")
    else:
        print(f"No hay actividades registradas en {dia} a las {hora}.")

    return agenda

# Punto 10: invertir diccionario pais->capital para capital->pais

def invertir_paises_capitales():

    print("\n--- Punto 10: Invertir diccionario países->capitales ---")
    paises_capitales = {
        "Argentina": "Buenos Aires",
        "Brasil": "Brasilia",
        "Chile": "Santiago",
        "Peru": "Lima"
    }

    capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}

    print("Países -> Capitales:", paises_capitales)
    print("Capitales -> Países:", capitales_paises)

    return paises_capitales, capitales_paises

# Desafío extra (solicitado): guardar y cargar datos en JSON

def desafio_extra_guardar_json(datos_a_guardar, nombre_archivo="datos_tp6.json"):

    print("\n--- Desafío extra: Guardar y cargar datos en JSON ---")
    # Preparar estructura serializable (convertir tuplas que deben ser listas)
    serializable = {}
    # datos_a_guardar es un diccionario con claves descriptivas.
    for clave, valor in datos_a_guardar.items():
        # Convertir tuplas dentro de diccionarios o listas a listas para JSON
        if isinstance(valor, dict):
            nuevo_dict = {}
            for k, v in valor.items():
                # Si la clave es tupla, convertir a string para JSON 
                if isinstance(k, tuple):
                    k_serial = json.dumps(k, ensure_ascii=False)
                else:
                    k_serial = str(k)
                # Si el valor es tupla, convertir a lista
                if isinstance(v, tuple):
                    nuevo_dict[k_serial] = list(v)
                else:
                    nuevo_dict[k_serial] = v
            serializable[clave] = nuevo_dict
        else:
            serializable[clave] = valor

    # Guardar en archivo
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            json.dump(serializable, f, ensure_ascii=False, indent=2)
        print(f"Datos guardados en '{nombre_archivo}'.")
    except Exception as e:
        print("Error al guardar en JSON:", e)
        return False

    # Leer nuevamente para verificar
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            cargado = json.load(f)
        print(f"Datos cargados correctamente desde '{nombre_archivo}'.")
        # Mostrar una clave de ejemplo para confirmar
        claves = list(cargado.keys())
        if claves:
            ejemplo_clave = claves[0]
            print(f"Ejemplo de contenido cargado para la clave '{ejemplo_clave}':")
            print(cargado[ejemplo_clave])
        return True
    except Exception as e:
        print("Error al leer desde JSON:", e)
        return False

# Función main: 

def main():
    # Puntos 1-3
    precios_frutas, lista_frutas = ejercicios_frutas()

    # Punto 4
    contactos = agenda_contactos()

    # Punto 5
    palabras_unicas, frecuencias = analizar_frase()

    # Punto 6
    alumnos, promedios = notas_alumnos()

    # Punto 7
    parcial1, parcial2, ambos, solo_uno, al_menos_uno = procesar_aprobados()

    # Punto 8
    stock = gestionar_stock()

    # Punto 9
    agenda = agenda_eventos()

    # Punto 10
    paises_capitales, capitales_paises = invertir_paises_capitales()

    # Desafío extra: 
    datos_para_guardar = {
        "precios_frutas": precios_frutas,
        "lista_frutas": lista_frutas,
        "contactos": contactos,
        "frecuencias_frase": frecuencias,
        "alumnos_notas": alumnos,
        "promedios": promedios,
        "parcial1": list(parcial1),
        "parcial2": list(parcial2),
        "stock": stock,
        "agenda": agenda,
        "paises_capitales": paises_capitales,
        "capitales_paises": capitales_paises
    }

    # Ejecutar guardado 
    desafio_extra_guardar_json(datos_para_guardar)

if __name__ == "__main__":
    main()
