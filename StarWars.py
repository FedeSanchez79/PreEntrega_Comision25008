# Pre-Entrega
# Ejercicio 1: Crear un programa que permita agregar productos a una lista y mostrarlos en pantalla.

from colorama import init, Fore, Style
init(autoreset=True)

# lista vacia para almacenar los productos
productos = []

# creo una funcion para agregar productos
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
                    print(Fore.RED +"Categoría no válida. Use: COMIC, COLECCIONABLE o SABLE DE LUZ.")
                else:
                    break

            while True:
                try:
                    precio = int(input("Ingrese el precio (sin centavos): "))
                    if precio < 0:
                        print(Fore.RED +"El precio no puede ser negativo.")
                        continue
                    break
                except ValueError:
                    print(Fore.RED +"Debe ingresar un número entero válido.")

            productos.append({
                "nombre": nombre.lower(),
                "categoria": categoria,
                "precio": precio
            })
            print(Fore.GREEN +f"Producto {nombre.upper()} agregado correctamente.")

            otra = input(Fore.CYAN + "¿Desea agregar otro producto? (SI/NO): ").strip().lower()
            if otra != "si":
                break
        except Exception as e:
            print(Fore.RED +f"Error al agregar producto: {e}")

 # creo una funcion para mostrar productos           

def mostrar_productos():
    if not productos:
        print(Fore.RED +"No hay productos en la tienda.")
    else:
        for i, producto in enumerate(productos, 1):
            print(Fore.GREEN +f"{i}. Nombre: {producto['nombre'].upper()}, Categoría: {producto['categoria'].upper()}, Precio: ${producto['precio']}")
        print(Fore.YELLOW +f"Total de productos: {len(productos)}")

# creo una funcion para buscar un productos

def buscar_producto():
    nombre = input("Ingrese el nombre del producto a buscar: ").strip().lower()
    encontrados = [p for p in productos if p["nombre"] == nombre]
    if encontrados:
        for p in encontrados:
            print(Fore.GREEN +f"Producto encontrado: Nombre: {p['nombre'].upper()}, Categoría: {p['categoria'].upper()}, Precio: ${p['precio']}")
    else:
        print(Fore.RED +"Producto no encontrado.")

# creo una funcion para eliminar productos

def eliminar_producto():
    if not productos:
        print(Fore.RED +"No hay productos para eliminar.")
        return
    mostrar_productos()
    try:
        indice = int(input("Ingrese el número del producto a eliminar: "))
        if 1 <= indice <= len(productos):
            eliminado = productos.pop(indice - 1)
            print(Fore.GREEN +f"Producto {eliminado['nombre'].upper()} eliminado correctamente.")
        else:
            print(Fore.RED +"Número inválido.")
    except ValueError:
        print(Fore.RED +"Debe ingresar un número entero válido.")
    except Exception as e:
        print(Fore.RED +f"Error al eliminar producto: {e}")

# Menú principal con las funciones disponibles
while True:
    print(Fore.LIGHTMAGENTA_EX +"\n" + "BIENVENIDO A LA TIENDA DE STAR WARS")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    try:
        opcion = int(input(Fore.CYAN +"Seleccione una opción: "))
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
                print(Fore.CYAN +"Gracias por usar la tienda. ¡Hasta luego!")
                break
            case _:
                print(Fore.RED +"Opción no válida.")
    except ValueError:
        print(Fore.RED +"Por favor, ingrese un número válido.")