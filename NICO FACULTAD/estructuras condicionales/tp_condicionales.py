#mayor de edad
edad=int(input("ingrese su edad: "))

if edad>=18 :
    print("eres mayor de edad")
else:
    print("eres menor de edad")

#aprobado o no
nota=int(input("ingrese su nota: "))

if nota>=6 :
    print("aprbado")
else:
    print("desaprobado")

#par o no
numero=int(input("ingrese un numero: "))

if numero % 2 == 0  :
    print("numero par")
else:
    print("numero inpar")

#edades gral
edad=int(input("ingrese su edad: "))

if edad<12 :
    print("eres un niño/a")
elif edad >= 12 and edad < 18:
    print("eres adolecente")
elif edad >= 18 and edad < 30:
    print("eres uun joven/adulto")
elif edad >= 30:
    print("eres adulto" )

#contraseña

contra=input("ingrese una contraseña que tenga entre 8 a 16 caracteres; ")
longitud_contra=len(contra)

if longitud_contra <= 16 >=8 :
    print("contraseña correcta ")

else:
    print("contraseña incorrecta")

#moda,media,mediana

import statistics as stats
import random

# Lista de ejemplo
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = stats.mode(numeros_aleatorios)
mediana = stats.median(numeros_aleatorios)
media = stats.mean(numeros_aleatorios)

print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media}")

if media > mediana > moda:
    print("Sesgo positivo (asimetría a la derecha)")
elif media < mediana < moda:
    print("Sesgo negativo (asimetría a la izquierda)")
else:
    print("No hay sesgo (distribución simétrica o caso ambiguo)")

#vocales !

palabra=input("ingrese una palabra: ")

if palabra[-1].lower() in "aeiou":
    palabra += "!"
    print(f"resltuado {palabra}")
else:
    print(F"resultado {palabra}")

#nombre en mayusculas
nombre=input("ingrese su nombre: ")
print("que desae hacer con su nombre: \n " 
"1- poner en mayusculas \n" 
"2- poner en minusculas \n" 
"3- solo la primera letra en mayuscula ")
opcion=int(input("ingrese la opcion deseada: "))
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())

#escalas de terremotos
magnitud=float(input("ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print("muy leve")      
elif 3 <= magnitud < 4:
    print("leve")
elif 4 <= magnitud < 5:
    print("moderado")
elif 5 <= magnitud < 6:
    print("fuerte")
elif 6 <= magnitud < 7:
    print("Muy Fuerte")
elif 7 <= magnitud:
    print("Extremo")

#estaciones del año segun hemisferio
mes=int(input("ingrese el numero del mes (1-12): "))
hemisferio=input("ingrese su hemisferio (N para norte, S para sur): ").upper()
dia=int(input("ingrese el dia del mes (1-31): "))
if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes <= 3 and dia < 20):
        print("Es invierno")
    elif (mes == 3 and dia >= 20) or (mes <= 6 and dia < 21):
        print("Es primavera")
    elif (mes == 6 and dia >= 21) or (mes <= 9 and dia < 22):
        print("Es verano")
    elif (mes == 9 and dia >= 22) or (mes <= 12 and dia < 21):
        print("Es otoño")
elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (mes <= 3 and dia < 20):
        print("Es verano")
    elif (mes == 3 and dia >= 20) or (mes <= 6 and dia < 21):
        print("Es otoño")
    elif (mes == 6 and dia >= 21) or (mes <= 9 and dia < 22):
        print("Es invierno")
    elif (mes == 9 and dia >= 22) or (mes <= 12 and dia < 21):
        print("Es primavera")