#1er ejemplo "hola mundo"
print("hola mundo")

#2do ejercicio "hola "nombre" "
nombre=input("ingresa su nombre: ")
print("Hola",nombre)

#3er ejercicio " hola 'nombre + apellido + edad' "
nombre=input("ingrese su nombre porfavor: ")
apellido=input("ingrese su apellido porfavor: ")
edad=input("ingrese su edad porfavor: ")
print(f"Hola,{nombre} {apellido} tienes {edad} años!")

#4to ejercicio "radio de un circulo"
import math
radio=float(input("ingrese el radio de un circulo: "))
area=math.pi*radio**2
perimetro=2*math.pi*radio
print("El area del circulo es: ", area, "y el perimetro es: ", perimetro)  

#5TO EJERCICIO "SEGUNDOS EN HORAS"
segundos=int(input("Ingrese la cantidad de segundos: "))
minutos=segundos // 60
horas=minutos // 60 
minutos_restantes=minutos % 60
segundos_restantes=segundos % 60
print("La cantidad de horas es:", horas, ", minutos:", minutos_restantes, "y segundos:", segundos_restantes)

#6to EJERCICIO "TABLAS DE UN NUMERO"
numero=int(input("Ingrese un numero:  "))
print("La tabla de multiplicar del numero", numero, "es:")
print("1 x",numero,"es: ",1*numero)
print("2 x",numero,"es: ",2*numero)
print("3 x",numero,"es :",3*numero)
print("4 x",numero,"es :",4*numero)
print("5 x",numero,"es :",5*numero)
print("6 x",numero,"es :",6*numero)
print("7 x",numero,"es :",7*numero)
print("8 x",numero,"es :",8*numero)
print("9 x",numero,"es :",9*numero)
print("10 x",numero,"es :",10*numero)

#7tmo ejercicio "ingresar un numero != a 0 y sumarlo, restarlo,etc"
numero=int(input("ingrese un numero mas grande que 0: "))
numero_2=int(input("ingrese otro numero mas grande que 0: "))
if numero != 0 and numero_2 != 0:
 print("la suma de", numero, "por", numero_2, "es: ", numero + numero_2)  
 print("la resta de", numero, "por", numero_2, "es: ", numero - numero_2)
 print("la multiplicacion de", numero, "por", numero_2, "es: ", numero * numero_2)
 print("la division de", numero, "por", numero_2, "es: ", numero / numero_2)
else:
    print("Por favor, ingrese numeros mayores que 0.")

#8avo ejercicio "indice masa corporal"
peso=float(input("ingrese su peso en kg: "))
altura=float(input("ingrese su altura en metros: "))
imc=peso/(altura**2)
print("su indice de masa corporal es: ", imc)

#9eno ejercicio "de celius a fahrenheit"
grados=float(input("ingrese la temperatura en grados celsius: " ))
fahrenheit=(grados * 9/5) + 32
print("La temperatura en grados fahrenheit es: ", fahrenheit)

#10mo ejercicio "promedio de 3 numeros"
numero_1=int(input("Ingrese la primer nota: "))
numero_2=int(input("Ingrese la segunda nota: "))
numero_3=int(input("Ingrese la 3era nota: "))
promedio=(numero_1 + numero_2 + numero_3) / 3
if numero_1 == 0 or numero_2 == 0 or numero_3 == 0:
    print("su nota no puede ser negativa ni 0")  
else:
    print("El promedio de los tres numeros es:", promedio)
