#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
#range.

multiplos_de_4 = list(range(4, 101, 4))
print("Números múltiplos de 4 del 1 al 100:", multiplos_de_4)

#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
#penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
#indexing con números negativos!

elementos_favoritos = ["rugby", "música", "viajar", "amigos", "cine"]
print(elementos_favoritos)
print("El penúltimo elemento de la lista es:", elementos_favoritos[-2])

#3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
#pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior.
lista_vacia = []
lista_vacia.append(input("Ingresa la primera palabra: "))
lista_vacia.append(input("Ingresa la segunda palabra: "))
lista_vacia.append(input("Ingresa la tercera palabra: "))
print("Lista resultante:", lista_vacia)

#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
#respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
#en los videos o bien investigar cómo funciona el indexing con números negativos!
animales = ["perro", "gato", "conejo", "pez"]
print("Lista de animales original:", animales)
animales[1] = "loro"
animales[-1] = "oso"
print("Lista de animales modificada:", animales)

#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

#nuemros=[8,15,3,22,7]
#numeros.remove(max(numeros))
#print(numeros)
#El programa crea una lista de 5 nuemros y utiliza "numeros.remove(max(numero))" 
# para detectar el numero de mayor valor y eliminarlo de la lista. 
# y al finalizar imprimir la lista sin el numero de mayor valor osea "22".

#6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
#pantalla los dos primeros.
numeros = list(range(10, 31, 5))
print(numeros)
print("Los dos primeros números de la lista son:", numeros[:2])

#7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
#cualesquiera.
autos = ["sedan", "polo", "suran", "gol"]
print("Lista de autos original:", autos)
autos[1:3] = ["hailux", "bora"]
print("Lista de autos modificada:", autos)

#8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
#directamente. Imprimir la lista resultante por pantalla.

dobles=[]
dobles.append(5*2)
dobles.append(10*2) 
dobles.append(15*2)
print("Lista de dobles:", dobles)

#9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
#diferentes clientes:
#compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
#["agua"]]
#a) Agregar "jugo" a la lista del tercer cliente usando append.
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
#c) Eliminar "pan" de la lista del primer cliente.
#d) Imprimir la lista resultante por pantalla

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("jugo")
print(compras)
compras[1][1] = "tallarines"
print(compras)
compras[0].remove("pan")
print(compras)
print("Lista de compras modificada:", compras)

#10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
#Posición lista_anidada[0]: 15
# Posición lista_anidada[1]: True
 #Posición lista_anidada[2][0]: 25.5
 #Posición lista_anidada[2][1]: 57.9
 #Posición lista_anidada[2][2]: 30.6
 #Posición lista_anidada[3]: False
#Imprimir la lista resultante por pantalla.

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print("Lista anidada:", lista_anidada)