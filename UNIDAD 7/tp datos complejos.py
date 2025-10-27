# 1) Dado el diccionario precios_frutas
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
# 1450}
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300   
print(precios_frutas)

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print(precios_frutas)

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios.
lista_frutas = list(precios_frutas.keys())
print(lista_frutas)

# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.

contactos = {}
for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número telefónico: ")
    contactos[nombre] = numero

nombre_buscado = input("Ingrese el nombre del contacto a buscar: ")
if nombre_buscado in contactos:
    print("Número telefónico:", contactos[nombre_buscado])
else:
    print("Contacto no encontrado.")
    print(f"{numero} x {i} = {numero * i}") 
    
# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.
frase = input("Ingrese una frase: ")
palabras = frase.split()    
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)

contador_palabras = {}
for palabra in palabras:
    contador_palabras[palabra] = contador_palabras.get(palabra, 0) + 1
print("Cantidad de veces que aparece cada palabra:", contador_palabras)

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.

alumnos = {}
for i in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    notas = input("Ingrese las 3 notas del alumno separadas por comas: ")
    notas = tuple(map(float, notas.split(",")))
    alumnos[nombre] = notas

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es: {promedio}")

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir)
parcial_1 = {101, 102, 103, 104, 105}
parcial_2 = {104, 105, 106, 107, 108}
aprobados_ambos = parcial_1.intersection(parcial_2)
print("Estudiantes que aprobaron ambos parciales:", aprobados_ambos)

aprobados_solo_1 = parcial_1.difference(parcial_2)
print("Estudiantes que aprobaron solo el Parcial 1:", aprobados_solo_1)

aprobados_solo_2 = parcial_2.difference(parcial_1)
print("Estudiantes que aprobaron solo el Parcial 2:", aprobados_solo_2)

aprobados_totales = parcial_1.union(parcial_2)
print("Estudiantes que aprobaron al menos un parcial:", aprobados_totales)

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.
stock_productos = {}
while True:
    accion = input("Ingrese 'consultar', 'agregar' o 'nuevo' para gestionar el stock (o 'salir' para terminar): ").lower()
    if accion == 'salir':
        break
    elif accion == 'consultar':
        print(stock_productos)
        producto = input("Ingrese el nombre del producto a consultar: ")
        if producto in stock_productos:
            print(f"El stock de {producto} es: {stock_productos[producto]}")
        else:
            print("Producto no encontrado.")
    elif accion == 'agregar':
        print(stock_productos)
        producto = input("Ingrese el nombre del producto al que desea agregar stock: ")
        if producto in stock_productos:
            cantidad = int(input("Ingrese la cantidad a agregar: "))
            stock_productos[producto] += cantidad
            print(f"Nuevo stock de {producto}: {stock_productos[producto]}")
        else:
            print("Producto no encontrado.")
    elif accion == 'nuevo':
        print(stock_productos)
        producto = input("Ingrese el nombre del nuevo producto: ")
        cantidad = int(input("Ingrese la cantidad inicial de stock: "))
        stock_productos[producto] = cantidad
        print(f"Producto {producto} agregado con un stock de {cantidad}.")
    else:
        print("Acción no reconocida. Intente nuevamente.")
        
# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
agenda = {}
while True:
    accion = input("Ingrese 'agregar', 'consultar' o 'salir': ").lower()
    if accion == 'salir':
        break
    elif accion == 'agregar':
        dia = input("Ingrese el día (formato DD/MM): ")
        hora = input("Ingrese la hora (formato HH:MM): ")
        evento = input("Ingrese el evento: ")
        agenda[(dia, hora)] = evento
        print(f"Evento agregado para {dia} a las {hora}.")
    elif accion == 'consultar':
        dia = input("Ingrese el día (formato DD/MM): ")
        hora = input("Ingrese la hora (formato HH:MM): ")
        evento = agenda.get((dia, hora), "No hay evento programado.")
        print(f"Evento para {dia} a las {hora}: {evento}")
    else:
        print("Acción no reconocida. Intente nuevamente.")
        
# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.

paises_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Colombia": "Bogotá"
}

capitales_paises = {v: k for k, v in paises_capitales.items()}
print("Diccionario de capitales a países:")
print(capitales_paises)

