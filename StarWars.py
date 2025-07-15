# ENTREGA FINAL - TIENDA STAR WARS
# Este programa permite gestionar una tienda de productos relacionados con Star Wars.

import sqlite3
from colorama import init, Fore
init(autoreset=True)

# Crear la base de datos si no existe
conexion = sqlite3.connect("productos.db")
cursor = conexion.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS productos 
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                categoria TEXT NOT NULL,
                descripcion TEXT,
                precio INTEGER NOT NULL,
                cantidad INTEGER DEFAULT 0)""")
conexion.commit()
conexion.close()

# Funcion auxiliar para mostrar productos en formato tabla

def mostrar_tabla(productos):
    try:
        print(Fore.YELLOW + "\nLista de productos:")
        print(Fore.LIGHTBLACK_EX + "─" * 97)
        print(Fore.WHITE + f"{'Nº':<4}│{'NOMBRE':<20}│{'CATEGORÍA':<15}│{'DESCRIPCIÓN':<25}│{'PRECIO':<10}│{'CANTIDAD':<10}")
        print(Fore.LIGHTBLACK_EX + "─" * 97)
        for i, p in enumerate(productos, 1):
            print(Fore.YELLOW + f"{i:<4}│" + Fore.GREEN + f"{p[1].upper():<20}" + Fore.WHITE + "│" + Fore.GREEN + f"{p[2].upper():<15}" + Fore.WHITE + "│" + Fore.GREEN + f"{p[3]:<25}" + Fore.WHITE + "│" + Fore.LIGHTRED_EX + f"${p[4]:<9}" + Fore.WHITE + "│" + Fore.LIGHTBLUE_EX + f"{p[5]:<10}")
            print(Fore.LIGHTBLACK_EX + "─" * 97)
    except Exception as e:
        print(Fore.RED + f"Error al mostrar la tabla: {e}")
        
# Funciones principales

def solicitar_entero(mensaje):
    while True:
        try:
            valor = int(input(Fore.CYAN + mensaje))
            return valor
        except ValueError:
            print(Fore.RED + "Entrada inválida. Debe ingresar un número entero.")

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
                    print(Fore.RED + "Categoría inválida.")
            descripcion = input(Fore.CYAN + "Ingrese una descripción del producto: ").strip()
            precio = solicitar_entero("Ingrese el precio del producto: ")
            cantidad = solicitar_entero("Ingrese la cantidad disponible: ")
            conexion = sqlite3.connect("productos.db")
            cursor = conexion.cursor()
            cursor.execute("""INSERT INTO productos (nombre, categoria, descripcion, precio, cantidad) VALUES (?, ?, ?, ?, ?)""", (nombre, categoria, descripcion, precio, cantidad))
            conexion.commit()
            conexion.close()
            print(Fore.GREEN + "Producto agregado exitosamente.")
            otra = input(Fore.CYAN + "¿Desea agregar otro producto? (SI/NO): ").strip().lower()
            if otra != "si":
                break
        except Exception as e:
            print(Fore.RED + f"Error al agregar producto: {e}")

def mostrar_productos():
    try:
        conexion = sqlite3.connect("productos.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre, categoria, descripcion, precio, cantidad FROM productos")
        productos = cursor.fetchall()
        conexion.close()
        if productos:
            mostrar_tabla(productos)
        else:
            print(Fore.RED + "No hay productos registrados.")
    except Exception as e:
        print(Fore.RED + f"Error al mostrar productos: {e}")

def buscar_producto():
    while True:
        try:
            nombre = input("Ingrese el nombre del producto a buscar: ").strip().lower()
            conexion = sqlite3.connect("productos.db")
            cursor = conexion.cursor()
            cursor.execute("SELECT id, nombre, categoria, descripcion, precio, cantidad FROM productos WHERE LOWER(nombre) LIKE ?", (f"%{nombre}%",))
            productos = cursor.fetchall()
            conexion.close()
            if productos:
                mostrar_tabla(productos)
            else:
                print(Fore.RED + "Producto no encontrado.")
            otra = input(Fore.CYAN + "¿Desea buscar otro producto? (SI/NO): ").strip().lower()
            if otra != "si":
                break
        except Exception as e:
            print(Fore.RED + f"Error al buscar producto: {e}")
            break

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
            mostrar_tabla(productos)
            indice = solicitar_entero("Ingrese el número del producto a eliminar: ")
            if 1 <= indice <= len(productos):
                id_a_eliminar = productos[indice - 1][0]
                nombre_eliminado = productos[indice - 1][1]
                confirmar = input(Fore.CYAN + f"¿Seguro que desea eliminar el producto {nombre_eliminado.upper()}? (SI/NO): ").strip().lower()
                if confirmar == "si":
                    cursor.execute("DELETE FROM productos WHERE id = ?", (id_a_eliminar,))
                    conexion.commit()
                    print(Fore.GREEN + "Producto eliminado correctamente.")
                else:
                    print(Fore.YELLOW + "Eliminación cancelada.")
            else:
                print(Fore.RED + "Número inválido.")
            conexion.close()
            otra = input(Fore.CYAN + "¿Desea eliminar otro producto? (SI/NO): ").strip().lower()
            if otra != "si":
                break
        except Exception as e:
            print(Fore.RED + f"Error al eliminar producto: {e}")
            break

def editar_producto():
    try:
        while True:
            conexion = sqlite3.connect("productos.db")
            cursor = conexion.cursor()
            cursor.execute("SELECT id, nombre, categoria, descripcion, precio, cantidad FROM productos")
            productos = cursor.fetchall()
            if not productos:
                print(Fore.RED + "No hay productos para editar.")
                conexion.close()
                return
            mostrar_tabla(productos)
            indice = solicitar_entero("Ingrese el número del producto que desea editar: ")
            if 1 <= indice <= len(productos):
                producto = productos[indice - 1]
                id_producto = producto[0]
                print(Fore.CYAN + "\n¿Qué campo desea editar?")
                print("1. Nombre")
                print("2. Categoría")
                print("3. Descripción")
                print("4. Precio")
                print("5. Cantidad")
                campo = solicitar_entero("Seleccione una opción (1-5): ")
                columnas = ["nombre", "categoria", "descripcion", "precio", "cantidad"]
                if 1 <= campo <= 5:
                    columna = columnas[campo - 1]
                    nuevo_valor = input("Ingrese el nuevo valor: ").strip()
                    if columna in ["precio", "cantidad"]:
                        nuevo_valor = int(nuevo_valor)
                    confirmar = input(Fore.CYAN + f"¿Seguro que desea cambiar {columna.upper()} a '{nuevo_valor}'? (SI/NO): ").strip().lower()
                    if confirmar == "si":
                        cursor.execute(f"UPDATE productos SET {columna} = ? WHERE id = ?", (nuevo_valor, id_producto))
                        conexion.commit()
                        print(Fore.GREEN + "Producto actualizado correctamente.")
                    else:
                        print(Fore.YELLOW + "Edición cancelada.")
                else:
                    print(Fore.RED + "Opción de campo no válida.")
            else:
                print(Fore.RED + "Número inválido.")
            conexion.close()
            mostrar_productos()
            otra = input(Fore.CYAN + "¿Desea editar otro producto? (SI/NO): ").strip().lower()
            if otra != "si":
                break
    except Exception as e:
        print(Fore.RED + f"Error al editar producto: {e}")

# Menú principal
while True:
    try:
        print(Fore.LIGHTMAGENTA_EX + "\nBIENVENIDO A LA TIENDA DE STAR WARS")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Buscar producto")
        print("4. Eliminar producto")
        print("5. Editar producto")
        print("6. Salir")

        opcion = solicitar_entero("Seleccione una opción: ")
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
                editar_producto()
            case 6:
                print(Fore.CYAN + "Gracias por usar la tienda. ¡Hasta luego!")
                break
            case _:
                print(Fore.RED + "Opción no válida.")
    except Exception as e:
        print(Fore.RED + f"Error en el menú principal: {e}")