import random

alumnos = [
    "Valentina De Los ángeles Albizú",
    "Pablo Andres Allende",
    "Luca Valentín Argumedo",
    "Pablo Avalos",
    "Lucas Avila",
    "Santino Barone",
    "Sofia Blangetti",
    "Nicolás Bohm",
    "Renzo Valentino Borello Canizo",
    "Juan Manuel Carrillo Taglio",
    "Facundo Gustavo Chacon Catalan",
    "Agustin Emiliano Contardi",
    "Jeronimo Coronel Alvarez",
    "Gabriel Emiliano Denis",
    "Facundo Gustavo Deseff",
    "Juan Martin García",
    "Enzo Giaquinta",
    "Sabrina Gimenez",
    "Joaquin Godoy",
    "Lucas Facundo Godoy",
    "Santino Alejo Godoy Galdeano",
    "Valentina Antonela Gordillo Moreno",
    "Lautaro Agustin Guardatti Esquivel",
    "Tiago Nahuel Guillot Duran",
    "Mateo Lautaro Liendo",
    "Juan Ignacio Martinez Quiroga",
    "Maximo Exequiel Monardez",
    "Tomas Agustin Mora Gonzalez",
    "Pablo Isaias Morinigo Lima",
    "Ares Martín Ocaña Martinez",
    "Thiago Santino Oviedo Saldaño",
    "Amanda Lucrecia Pagano",
    "Máximo Juan Cruz Quiroga",
    "Facundo Agustín Ramírez García",
    "Franco Agustin Rios Alzamora",
    "Leonel Enrique Rojas",
    "Matias Nicolas Ruiz Vargas",
    "Ramiro Ezequiel Salcedo",
    "Ismael Saleme Padolsky",
    "Ignacio Exequiel Sanchez",
    "Fabrizio Jonathan Simon Santos",
    "Cristian Gabriel Soto",
    "Giovanna Mercedes Suarez",
    "Ismael Mauricio Suarez",
    "Fernando Agustín Torrez",
    "Luca Nicolas Valdez",
    "Tiziano Ignacio Valentini",
    "Matias Nicolas Vargas",
    "Juan Ignacio Videla Continella",
    "Pablo Exequiel Avalos"
]

indices = list(range(len(alumnos)))
random.shuffle(indices)


alumnos_reordenados = []
for i in indices:
    alumnos_reordenados.append(alumnos[i])


matriz_indices = []
matriz_alumnos = []

for i in range(0, len(indices), 4):
    matriz_indices.append(indices[i:i+4])
    matriz_alumnos.append(alumnos_reordenados[i:i+4])


print("Matriz de índices aleatorios:")
for fila in matriz_indices:
    print(fila)

print("\nMatriz de alumnos reordenados:")
for fila in matriz_alumnos:
    print(fila)
