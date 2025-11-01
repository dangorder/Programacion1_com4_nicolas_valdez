# 1. Crear archivo inicial con productos: Crear un archivo de texto llamado
# productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad
with open('productos.txt', 'w') as file:
    file.write('Manzana,$5000,3kg\n')
    file.write('Banana,$1300,0.5kg\n')
    file.write('Naranja,$3000,1kg\n')
    print("Archivo 'productos.txt' creado correctamente.")


# 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
# línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
# formato: Producto: Lapicera | Precio: $120.5 | Cantidad: 30
with open('productos.txt', 'r') as file:
    for line in file:
        nombre, precio, cantidad = line.strip().split(',')
        print(f'Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad}')
print()

# 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
# los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
# cantidad) y lo agregue al archivo sin borrar el contenido existente.
nuevo_producto = input("Ingrese un nuevo producto (nombre,precio,cantidad): ")
with open('productos.txt', 'a') as file:
    file.write(nuevo_producto + '\n')
print("Nuevo producto agregado correctamente.")
print(f"Contenido actualizado de 'productos.txt':")
with open('productos.txt', 'r') as file:
    for line in file:
        print(line.strip())
print()

# 4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
# una lista llamada productos, donde cada elemento sea un diccionario con claves:
# nombre, precio, cantidad.
productos = []
with open('productos.txt', 'r') as file:
    for line in file:
        nombre, precio, cantidad = line.strip().split(',')
        producto = {
            'nombre': nombre,
            'precio': precio,
            'cantidad': cantidad
        }
        productos.append(producto)
print("Lista de productos como diccionarios:")
for producto in productos:
    print(producto)
print()

# 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
# producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
# no existe, mostrar un mensaje de error.
busqueda = input("Ingrese el nombre del producto a buscar: ")
encontrado = False
for producto in productos:
    if producto['nombre'].lower() == busqueda.lower():
        print(f"Producto encontrado: {producto}")
        encontrado = True
        break
if not encontrado:
    print("Error: Producto no encontrado.")
print()

# 6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
# productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
# productos actualizados desde la lista.
with open('productos.txt', 'w') as file:
    for producto in productos:
        linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
        file.write(linea)
print("Archivo 'productos.txt' actualizado correctamente.")
print(f"Contenido final de 'productos.txt':")
with open('productos.txt', 'r') as file:
    for line in file:
        print(line.strip())

