alumnos = []
asistencias = []
opcion = 0
while opcion != 8:
    print("\n MENU GESTION DE ASISTENCIAS ")
    print (" 1. Ingresar nombres de estudiantes")
    print (" 2. Mostrar listado con asistencia")
    print (" 3. Consultar asistencias por estudiantes ")
    print (" 4. Mostrar estudiantes con asistencia 0")
    print (" 5. Agregar estudiante")
    print (" 6. Marcar asistencia")
    print (" 7. Ver todos los estudiantes")
    print (" 8. SALIR")

    opcion = input("Ingrese una opcion: ")
    if opcion.isdigit:
        opcion = int(opcion)
    else: 
        print("Debe ingresar un numero del 1 al 8")

    if opcion == 1:
        cantidad = input(" ¿Cuantos estudiantes desea ingresar? ")
        if cantidad.isdigit():
            cantidad = int(cantidad) 
            for i in range(cantidad):
                nombre = input("Ingrese el nombre del estudiante: ").strip()
                if nombre != "" and nombre not in alumnos:
                    alumnos.append(nombre)
                    asistencias.append(0)
                else:
                    print (" Nombre vacio o ya ingresado ")
        else:
            print("Ingrese un numero valido: ")
    elif opcion == 2:
        print(" \n LISTADO DE ASISTENCIA ")
        for i in range (len(alumnos)):
            print(alumnos[i], ":", asistencias[i], "asistencias ")
    elif opcion == 3:
        nombre = input("Ingrese el nombre del estudiante: ").strip()
        if nombre in alumnos:
            i = alumnos.index(nombre)
            print(nombre, "tiene", asistencias[i], "asistencias")
        else:
            print("Estudiante no encontrado. ")
    elif opcion == 4:
        print("\n ESTUDIANTES CON ASISTENCIA 0: " )
        for i in range(len(alumnos)):
            if asistencias[i]==0:
                print(alumnos[i])
    elif opcion == 5:
        nombre=input("Ingrese el nombre del estudiante: ").strip()
        if nombre!= ""and nombre not in alumnos:
            alumnos.append(nombre)
            asistencias.append(0)
            print("Estudiante agregado. ")
        else:
            print("Estudiante ya existente o nombre vacio. ")

    elif opcion == 6:
        nombre=input("Ingrese el nombre del estudiante para marcar asistencia: ").strip()
        if nombre in alumnos:
            i = alumnos.index(nombre)
            asistencias[i] += 1
            print("Se marco asistencia a:", nombre)
        else:
            print("Estudiante no encontrado")
    elif opcion == 7:
        print("\n TODOS LOS ESTUDIANTES")
        for i in range(len(alumnos)):
            print(alumnos[i], ":", asistencias[i], "asistencias")
    elif opcion == 8:
        print("Saliendo del programa")
    else:
        print("Opcion invalida")

