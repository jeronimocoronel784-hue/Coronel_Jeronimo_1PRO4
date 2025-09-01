import random
opciones = ["piedra" , "papel" , "tijera"]
jugador_gana = 0
compu_gana = 0
while True:
     print("Menu")
     print("1 PIEDRA")
     print("2 PAPWL")
     print("3 TIJERA")
     print("4 SALIR")
     eleccion = input("Ingrese una opcion (1-4): ")

      if eleccion == "4":
      print("El juego ha sido terminado")   
      print(f"El jugador gano {jugador_gana} veces.")
      print(f"La maquina gano {compu_gana} veces. ")
        break

