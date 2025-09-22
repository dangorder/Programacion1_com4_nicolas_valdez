excursiones=[]
cupos=[]

while True:

    print("1. agregar excursiones disponibles")
    print("2. agregar cu pos de las excursiones")
    print("3.mostrar lista de excursiones disponibles y sus cupos")
    print("4.buscar un aexcursion y verificar sus cupos")
    print("5. mostrar excursiones sin cupos disponibles")
    print("6. actualizar cupos de una excursion")
    print("7. salir del sistema")

    eleccion=int(input("seleccione una opcion del menu:  "))

    if eleccion == 1:
        excursion=input("ingrese la nueva excursion: ")
        excursiones.append(excursion)
        cupos.append(0)
        print (" excursion ingresada correctamente")
        print("")
    
    elif eleccion == 2:
        print(excursiones)
        excursion=input("ingrese el nombre de la excursion a la que desea darle mas cupos: ")
        if excursion in excursiones:
            cupo= int(input(f"ingrese la cantidad de cupos que desdea agregarle a {excursion}: "))
            indice= excursiones.index(excursion)
            cupos[indice]   += cupo
            print("cupos agregados exitosamente")
        else: 
            print("la excursion no esta ingresada")

        print("")
    
    elif eleccion == 3:

        for i in range(len(excursiones)):
            print(f"excursiones: {excursiones[i]}, cupos disponible: {cupos[i]}")
        print("")

    elif eleccion == 4:
        print(excursiones)
        excursion=input("de que excursion le gustaria saber los cupos disponibles: ")
        if excursion in excursiones:
            indice= excursiones.index(excursion)
            print(F"la excursion {excursion} tiene {cupos[indice]} cupos disponibles.. ") 
        else:
            print("la excursion no esta ingresada")
        print("")

    elif eleccion== 5:
        print(" las excursiones sin cupos son: ")

        for i in range(len(excursiones)):
            if cupos[i] == 0:
                print("excisones: ", excursiones[i])
            else:
                print("no hay excursiones sin cupos disponibles")
        print("")

    elif eleccion == 6:
        print(excursiones)
        excursion=input("ingrese la excursion a la que desea cambiarle los cupos: ")
        if excursion in excursiones:
            nuevo_cupo=int(input(" ingrese la cantidad de  cupos nueva: "))
            indice= excursiones.index(excursion)
            cupos[indice] = nuevo_cupo
            print("cupos actualizados exitosamente")
            print(f"la excursion {excursion} ahora tiene {cupos[indice]} cupos disponibles")
        else:
            print("la excursion no esta ingresada")
        print("")
    
    elif eleccion == 7:
        print("saliendo del sistema.................")
        break



