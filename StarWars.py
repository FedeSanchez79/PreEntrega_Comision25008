# ENTREGA FINAL: TIENDA DE STAR WARS
# Integración de SQLite y Colorama para una tienda de productos de Star Wars.

import sqlite3
conexion = sqlite3.connect("productos.db")
print("Conexión a la base de datos establecida.")
cursor = conexion.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        categoria TEXT NOT NULL,
        precio INTEGER NOT NULL
    )
""")
conexion.commit()

import sqlite3
from colorama import init, Fore, Style
init(autoreset=True)

# Creo una función para agregar productos
def agregar_producto():
    while True:
        try:
            nombre = input("Ingrese el nombre del producto: ").strip()
            if not nombre:
                print("Debe agregar un nombre.")
                continue

            while True:
                categoria = input("Ingrese su categoría (COMIC/COLECCIONABLE/SABLE DE LUZ): ").strip().lower()
                if categoria not in ("comic", "coleccionable", "sable de luz"):
                    print(Fore.RED + "Categoría no válida. Use: COMIC, COLECCIONABLE o SABLE DE LUZ.")
                else:
                    break

            while True:
                try:
                    precio = int(input("Ingrese el precio (sin centavos): "))
                    if precio < 0:
                        print(Fore.RED + "El precio no puede ser negativo.")
                        continue
                    break
                except ValueError:
                    print(Fore.RED + "Debe ingresar un número entero válido.")

            # Insertar en la base de datos
            conexion = sqlite3.connect("productos.db")
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO productos (nombre, categoria, precio) VALUES (?, ?, ?)",
                           (nombre.lower(), categoria, precio))
            conexion.commit()
            conexion.close()

            print(Fore.GREEN + f"Producto {nombre.upper()} agregado correctamente.")

            otra = input(Fore.CYAN + "¿Desea agregar otro producto? (SI/NO): ").strip().lower()
            if otra != "si":
                break
        except Exception as e:
            print(Fore.RED + f"Error al agregar producto: {e}")

# Mostrar productos desde la base de datos
def mostrar_productos():
    try:
        conexion = sqlite3.connect("productos.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre, categoria, precio FROM productos")
        productos = cursor.fetchall()
        conexion.close()

        if not productos:
            print(Fore.RED + "No hay productos en la tienda.")
        else:
            for i, producto in enumerate(productos, 1):
                print(Fore.GREEN + f"{i}. Nombre: {producto[1].upper()}, Categoría: {producto[2].upper()}, Precio: ${producto[3]}")
            print(Fore.YELLOW + f"Total de productos: {len(productos)}")
    except Exception as e:
        print(Fore.RED + f"Error al mostrar productos: {e}")

# Buscar producto por nombre
def buscar_producto():
    nombre = input("Ingrese el nombre del producto a buscar: ").strip().lower()
    try:
        conexion = sqlite3.connect("productos.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT nombre, categoria, precio FROM productos WHERE nombre = ?", (nombre,))
        productos = cursor.fetchall()
        conexion.close()

        if productos:
            for p in productos:
                print(Fore.GREEN + f"Producto encontrado: Nombre: {p[0].upper()}, Categoría: {p[1].upper()}, Precio: ${p[2]}")
        else:
            print(Fore.RED + "Producto no encontrado.")
    except Exception as e:
        print(Fore.RED + f"Error al buscar producto: {e}")

# Eliminar producto por número
def eliminar_producto():
    try:
        conexion = sqlite3.connect("productos.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre, categoria, precio FROM productos")
        productos = cursor.fetchall()

        if not productos:
            print(Fore.RED + "No hay productos para eliminar.")
            conexion.close()
            return

        for i, producto in enumerate(productos, 1):
            print(Fore.GREEN + f"{i}. Nombre: {producto[1].upper()}, Categoría: {producto[2].upper()}, Precio: ${producto[3]}")

        indice = int(input("Ingrese el número del producto a eliminar: "))
        if 1 <= indice <= len(productos):
            id_a_eliminar = productos[indice - 1][0]
            cursor.execute("DELETE FROM productos WHERE id = ?", (id_a_eliminar,))
            conexion.commit()
            print(Fore.GREEN + f"Producto {productos[indice - 1][1].upper()} eliminado correctamente.")
        else:
            print(Fore.RED + "Número inválido.")
        conexion.close()
    except ValueError:
        print(Fore.RED + "Debe ingresar un número entero válido.")
    except Exception as e:
        print(Fore.RED + f"Error al eliminar producto: {e}")

# Menú principal con las funciones disponibles
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

conexion.close()
