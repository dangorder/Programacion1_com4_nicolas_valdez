#Un curso necesita un sistema para registrar los alumnos y llevar un conteo de sus asistencias a clase. 
# Se pide programar un menú que utilice listas paralelas: una lista alumnos[] 
# para almacenar los nombres de los estudiantes (e.g., "Juan Pérez", "María García", "Carlos López") 
# y otra lista asistencias[] para almacenar el número de asistencias de cada estudiante. 
# Ambas listas deben estar relacionadas por el índice, de manera que el número de 
# asistencias en asistencias[i] corresponda al estudiante en alumnos[i]. 
# El programa debe usar un bucle while para presentar un menú al usuario, 
# permitiéndole realizar diferentes operaciones hasta que elija la opción "Salir".

alumnos=[]
asistencia=[]


while True:
    print("1. agregar alumno")  
    print("2. registrar asistencia")
    print("3. mostrar alumnos y asistencias") 
    print("4. agregar varios alumnos")   
    print("5. consultar la asistencia de un alumno")
    print("6. lista de alumnos con asistencia == 0")
    print("7. salir")

    eleccion=int(input("ingrese una opcion: "))
    if eleccion == 1:
        nombre=input("ingrese el nombre del alumno: ")
        alumnos.append(nombre)
        asistencia.append(0)
        print("alumno agregado")
        print(alumnos)
        print(asistencia)   

        print("")
    
    elif eleccion == 2:
        nombre=input("ingrese el nombre del alumno: ")
        if nombre in alumnos:
            indice=alumnos.index(nombre)
            asistencia[indice] += 1
            print("asistencia registrada")
            print("")
        else:
            print("el alumno no esta registrado")
        print(alumnos)
        print(asistencia)

        print("")

    elif eleccion== 3:
        print(alumnos)
        print (asistencia)
        print("")

    elif eleccion == 4:
        cantidad=int(input("ingrese la cantidad de alumnos a agregar: "))
        for i in range(cantidad):
            nombre=input("ingrese el nombre del alumno: ")
            alumnos.append(nombre)
            asistencia.append(0)
        print("alumnos agregados")
        print(alumnos)
        print(asistencia)
        print("")
    

    elif eleccion == 5:
        nombre=input("ingrese el nombre del alumno: ")
        if nombre in alumnos:
            indice=alumnos.index(nombre)
            print(f"el alumno {nombre} tiene {asistencia[indice]} asistencias")
            print("")
        else:
            print("el alumno no esta registrado")
        print(alumnos)
        print(asistencia)
        print("")
    
    elif eleccion == 6 :
        print("alumnos con asistencia == 0")
        for i in range(len(alumnos)):
            if asistencia[i]== 0:
                print(alumnos[i], asistencia[i])
        print("")

    elif eleccion == 7: 
        print("saliendo del programa")
        break

    else:
        print("opcion no valida, intente de nuevo")