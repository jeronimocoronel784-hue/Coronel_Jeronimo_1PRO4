import random
def elegir_palabra():
    palabras=["python", "programacion", "teclado", "computadora", "algoritmo", "software", "tecnologia"]
    return random.choice(palabras)

def mostrar_palabra(palabra_secreta, letras_adivinadas):
    estado=""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            estado += letra + ""
        else:
            estado += "_"
    return estado.strip()

def jugar_ahorcado():
    palabra = elegir_palabra()
    letras_adivinadas = []  # Lista de letras que el jugador ya intento
    intentos = 6            # Numero máximo de errores permitidos

    print(" Estas jugando Ahorcado ")
    print("Tienes que adivinar la palabra secreta.")
    print("La palabra tiene", len(palabra), "letras.")
    print(mostrar_palabra(palabra, letras_adivinadas))

    while intentos > 0:
        letra = input("Ingresa una letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print(" Ingresa solo una letra valida.")
            continue

        if letra in letras_adivinadas:
            print(" Ya se ingreso esa letra, pruebe con otra.")
            continue

        letras_adivinadas.append(letra)

        if letra in palabra:
            print(" Adivinaste una letra correctamente!")
        else:
            intentos -= 1
            print(f" Letra incorrecta. Te quedan {intentos} intentos.")

        estado_actual = mostrar_palabra(palabra, letras_adivinadas)
        print(estado_actual)

        if "_" not in estado_actual:
            print(" ¡Felicidades! Adivinaste la palabra:", palabra)
            break

    if intentos == 0:
        print(" Te quedaste sin intentos. La palabra era:", palabra)

if __name__ == "__main__":
    jugar_ahorcado()
