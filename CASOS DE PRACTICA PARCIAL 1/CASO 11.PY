ordenes= []
tiempo_estimado= []

while True:

    print("1. agregar orden")
    print("2.agrerar tiempo estimado a una orden especifica")
    print("3.mostrar ordenes y tiempos estimados")
    print("4. consultar el tiempo de una orden especifica")
    print("5. lsita de ornedes sin tiempo estimado/ no diagnoticadas")
    print("6. actualizar el tiempo de una orden especifica")
    print("7. salir")

    eleccion=int(input("ingrese una opcion: "))

    if eleccion == 1:
        orden=int(input("ingrese el numero de la orden que desea agregar: "))
        ordenes.append(orden)
        tiempo_estimado.append(0)
        print("orden agregada exitosamente")
        print("")
    
    elif eleccion == 2: 
        print(ordenes)
        orden=int(input("ingrese el numero de la orden a la que desea agregarle un tiempo estimado: "))
       
        if orden in ordenes: 
             tiempo=int(input("ingrese el tiempo que desea agregar en minutos : "))
             indice= ordenes.index(orden)
             tiempo_estimado[indice]= tiempo
             print("tiempo estimado agregado exitosamente")
        else:
            print("la orden no existe")
            
        print("")

    elif eleccion == 3:
        for i in range(len(ordenes)):
            print(f"orden: {ordenes[i]}, tiempo estimado: {tiempo_estimado[i]} minutos")
        print("")
    
    elif eleccion == 4: 
        orden=int(input("ingrese el numero de orden al uqe desea consultar el tiempo estimado: "))
        if orden in ordenes:
            indice= ordenes.index(orden)
            print(f"el tiempo estimado para la orden {orden} es de {tiempo_estimado[indice]} minutos")
        print("")

    elif eleccion == 5:
        print("ordenes sin tiempo estimado / no diagnosticadas: ")
        for i in range(len(ordenes)):
            if tiempo_estimado == 0:
                print("orden:", ordenes[i])
        print("")

    elif eleccion == 6:
        orden=int(input("ingrese el numero de orden al que desea actualizar el tiempo: "))
        tiempo=int(input("ingrese el nuevo tiempo estimado: "))
        if orden in ordenes: 
            indice= ordenes.index(orden)
            tiempo_estimado[indice]= tiempo
            print("tiempo estimado actualizado exitosamente")
            print(f"el nuevo tiempo estimado para la orden {orden} es de {tiempo_estimado[indice]} minutos")
        print("")

    elif eleccion == 7 :
        print ("saliendo del sistema.....")
        break


