    # Pre-Entrega
# Ejercicio 1: Crear un programa que permita agregar productos a una lista y mostrarlos en pantalla.
productos = []

while True:
    cartel_bienvenida = "bienvenido a la vinoteca".upper()
    print(cartel_bienvenida)
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        nombre_producto = input("Ingrese el nombre del producto: ")
        precio_producto = int(input("Ingrese el precio del producto: "))
        cantidad_producto = int(input("Ingrese la cantidad del producto: "))
        productos.append({"nombre": nombre_producto.lower(), "precio": precio_producto, "cantidad": cantidad_producto})
    elif opcion == 2:
        if not productos:
            print("No hay productos en la tienda.")
        else:
            for producto in productos:
                print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
    elif opcion == 3:
        nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
        encontrado = False
        for producto in productos:
            if producto['nombre'] == nombre_buscar.lower():
                print(f"Producto encontrado: Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
                encontrado = True
                break
        if not encontrado:
            print("Producto no encontrado.")
    elif opcion == 4:
        nombre_eliminar = input("Ingrese el nombre del producto a eliminar: ")
        encontrado = False
        for producto in productos:
            if producto['nombre'].lower() == nombre_eliminar.lower():
                productos.remove(producto)
                print(f"Producto {nombre_eliminar} eliminado.")
                encontrado = True
                break
        if not encontrado:
            print("Producto no encontrado.")        
    elif opcion == 5:
        print("Gracias por usar la tienda. ¡Hasta luego!")
        break
    else:
        print("Opción no válida, intente nuevamente.")
