import random
opcion=0
while opcion != 4 : 
    print("1: piedra ")
    print("2: papel ")
    print("3: tijeras ")
    print("4: salir ")
    opcion=int(input("elija una opcion: "))

    eleccion=random.randint(1,4)
#piedra
    if opcion == 1 and eleccion == 1:
        print(f"elegiste {opcion}, y la cpu eligio {eleccion}")
        print("empate")
        
    elif opcion == 1 and eleccion == 2:
        print(f"elegiste {opcion}, y la cpu eligio {eleccion}")
        print("perdiste")
        
    elif opcion == 1 and eleccion == 3:
        print(f"elegiste {opcion}, y la cpu eligio {eleccion}")
        print("ganaste")
        
#papel
    if opcion == 2 and eleccion == 2:
        print(f"elegiste {opcion}, y la cpu eligio {eleccion}")
        print("empate")
        
    elif opcion == 2 and eleccion == 3:
        print(f"elegiste {opcion}, y la cpu eligio {eleccion}")
        print("perdiste")
        
    elif opcion == 2 and eleccion == 1:
        print(f"elegiste {opcion}, y la cpu eligio {eleccion}")
        print("ganaste")
        
#tijeras
    if opcion == 3 and eleccion == 3:
        print(f"elegiste {opcion}, y la cpu eligio {eleccion}")
        print("empate")
        
    elif opcion == 3 and eleccion == 1:
        print(f"elegiste {opcion}, y la cpu eligio {eleccion}")
        print("perdiste")
        
    elif opcion == 3 and eleccion == 2:
        print(f"elegiste {opcion}, y la cpu eligio {eleccion}")
        print("ganaste")
        

else:
    print("que aburrido")