# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.ç

for numero in range(101):
    print(numero)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

numero=int(input("ingrese un numero entero de mas de 1 cifra: "))
cifras=0
while numero != 0:          
    numero //= 10
    cifras += 1
print("El numero tiene", cifras, "cifras")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

num1=int(input("ingrese un numero: "))
num2=int(input("ingrese otro numero mayor que el anterior: "))
suma=0
for numero in range(num1 + 1, num2):
    suma += numero
print("La suma de los numeros entre", num1, "y", num2, "es:", suma)

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.
primer_numero=int(input("ingrese un numero entero: "))
suma=0
while primer_numero != 0:
    suma += primer_numero
    primer_numero=int(input("ingrese otro numero entero (o 0 para terminar): ")) 
print("La suma total es:", suma)

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
numero_aleatorio=random.randint(0,9)
intentos=0
adivina=-1
while adivina != numero_aleatorio:
    adivina=int(input("Adivina el numero entre 0 y 9: "))
    intentos += 1
    if adivina < numero_aleatorio:
        print("Demasiado bajo. Intenta de nuevo.")
    elif adivina > numero_aleatorio:
        print("Demasiado alto. Intenta de nuevo.")
print(f"Felicidades! Adivinaste el numero {numero_aleatorio} en {intentos} intentos.")


#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.
for numero in range(100, -1, -1):
    if numero % 2 == 0:
        print(numero)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.
numero=int(input("ingreese un nuemro entero para sumar todos los numeros entre 0 y ese numero: "))
suma=0
for i in range(numero + 1):
    suma += i   
print("La suma de los numeros entre 0 y", numero, "es:", suma)

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

pares=0
impares=0
positivos=0
negativos=0
for i in range(100):
    numero=int(input("ingrese un numero entero: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
print("Cantidad de numeros pares:", pares)
print("Cantidad de numeros impares:", impares)
print("Cantidad de numeros positivos:", positivos)
print("Cantidad de numeros negativos:", negativos)

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).

suma=0
for i in range(100): 
    numero=int(input("ingrese un numero entero: "))
    suma += numero  
media=suma / 100
print("La media de los numeros ingresados es:", media)

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
numero=int(input("ingrese un numero entero para invertir sus cifras: "))
numero_invertido=0  
while numero > 0:
    digito=numero % 10
    numero_invertido=numero_invertido * 10 + digito
    numero //= 10
print("El numero invertido es:", numero_invertido)



