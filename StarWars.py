# ENTREGA FINAL - TIENDA STAR WARS
# Este programa permite gestionar una tienda de productos relacionados con Star Wars.

import sqlite3
from colorama import init, Fore
init(autoreset=True)

conexion = sqlite3.connect("productos.db")
cursor = conexion.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        categoria TEXT NOT NULL,
        descripcion TEXT,
        precio INTEGER NOT NULL,
        cantidad INTEGER DEFAULT 0
    )
""")


conexion.commit()
conexion.close()

# Función para agregar productos
def agregar_producto():
    while True:
        try:
            nombre = input(Fore.CYAN + "Ingrese el nombre del producto: ").strip().lower()
            categorias_validas = ["comic", "coleccionable", "sable de luz"]
            while True:
                categoria = input(Fore.CYAN + "Ingrese la categoría (comic / coleccionable / sable de luz): ").strip().lower()
                if categoria in categorias_validas:
                    break
                else:
                    print(Fore.RED + "Categoría inválida. Debe ingresar una de las siguientes opciones: COMIC / COLECCIONABLE / SABLE DE LUZ")
            descripcion = input(Fore.CYAN + "Ingrese una descripción del producto: ").strip()
            precio = int(input(Fore.CYAN + "Ingrese el precio del producto: "))
            cantidad = int(input(Fore.CYAN + "Ingrese la cantidad disponible: "))

            conexion = sqlite3.connect("productos.db")
            cursor = conexion.cursor()
            cursor.execute("""
                INSERT INTO productos (nombre, categoria, descripcion, precio, cantidad)
                VALUES (?, ?, ?, ?, ?)
            """, (nombre, categoria, descripcion, precio, cantidad))
            conexion.commit()
            conexion.close()

            print(Fore.GREEN + "Producto agregado exitosamente.")
            otra = input(Fore.CYAN + "¿Desea agregar otro producto? (SI/NO): ").strip().lower()
            if otra != "si":
                break
        except ValueError:
            print(Fore.RED + "Error: El precio y la cantidad deben ser números enteros.")
        except Exception as e:
            print(Fore.RED + f"Error al agregar producto: {e}")
            break

# Función para mostrar productos
def mostrar_productos():
    try:
        conexion = sqlite3.connect("productos.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT nombre, categoria, descripcion, precio, cantidad FROM productos")
        productos = cursor.fetchall()
        conexion.close()

        if productos:
            print(Fore.YELLOW + "\nLista de productos:")
            for p in productos:
                print(Fore.GREEN + f"Nombre: {p[0].upper()}, Categoría: {p[1].upper()}, Descripción: {p[2]}, Precio: ${p[3]}, Cantidad: {p[4]}")
        else:
            print(Fore.RED + "No hay productos registrados.")
    except Exception as e:
        print(Fore.RED + f"Error al mostrar productos: {e}")

# Función para buscar producto por nombre
def buscar_producto():
    while True:
        nombre = input("Ingrese el nombre del producto a buscar: ").strip().lower()
        try:
            conexion = sqlite3.connect("productos.db")
            cursor = conexion.cursor()
            cursor.execute("SELECT nombre, categoria, descripcion, precio, cantidad FROM productos WHERE nombre = ?", (nombre,))
            productos = cursor.fetchall()
            conexion.close()

            if productos:
                for p in productos:
                    print(Fore.GREEN + f"Producto encontrado: Nombre: {p[0].upper()}, Categoría: {p[1].upper()}, Descripción: {p[2]}, Precio: ${p[3]}, Cantidad: {p[4]}")
            else:
                print(Fore.RED + "Producto no encontrado.")

            otra = input(Fore.CYAN + "¿Desea buscar otro producto? (SI/NO): ").strip().lower()
            if otra != "si":
                break
        except Exception as e:
            print(Fore.RED + f"Error al buscar producto: {e}")
            break

# Función para eliminar producto por número de lista
def eliminar_producto():
    while True:
        try:
            conexion = sqlite3.connect("productos.db")
            cursor = conexion.cursor()
            cursor.execute("SELECT id, nombre, categoria, descripcion, precio, cantidad FROM productos")
            productos = cursor.fetchall()

            if not productos:
                print(Fore.RED + "No hay productos para eliminar.")
                conexion.close()
                return

            print(Fore.YELLOW + "\nLista de productos:")
            for i, producto in enumerate(productos, 1):
                print(Fore.GREEN + f"{i}. Nombre: {producto[1].upper()}, Categoría: {producto[2].upper()}, Descripción: {producto[3]}, Precio: ${producto[4]}, Cantidad: {producto[5]}")

            try:
                indice = int(input("Ingrese el número de orden del producto a eliminar: "))
                if 1 <= indice <= len(productos):
                    id_a_eliminar = productos[indice - 1][0]
                    nombre_eliminado = productos[indice - 1][1]
                    cursor.execute("DELETE FROM productos WHERE id = ?", (id_a_eliminar,))
                    conexion.commit()
                    print(Fore.GREEN + f"Producto {nombre_eliminado.upper()} eliminado correctamente.")
                else:
                    print(Fore.RED + "Número inválido. Intente nuevamente.")
                    continue  
            except ValueError:
                print(Fore.RED + "Debe ingresar un número entero válido.")
                continue

            conexion.close()

            otra = input(Fore.CYAN + "¿Desea eliminar otro producto? (SI/NO): ").strip().lower()
            if otra != "si":
                break
        except Exception as e:
            print(Fore.RED + f"Error al eliminar producto: {e}")
            break

# Menú principal
while True:
    print(Fore.LIGHTMAGENTA_EX + "\n" + "BIENVENIDO A LA TIENDA DE STAR WARS")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    try:
        opcion = int(input(Fore.CYAN + "Seleccione una opción: "))
        match opcion:
            case 1:
                agregar_producto()
            case 2:
                mostrar_productos()
            case 3:
                buscar_producto()
            case 4:
                eliminar_producto()
            case 5:
                print(Fore.CYAN + "Gracias por usar la tienda. ¡Hasta luego!")
                break
            case _:
                print(Fore.RED + "Opción no válida.")
    except ValueError:
        print(Fore.RED + "Por favor, ingrese un número válido.")
