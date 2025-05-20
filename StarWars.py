# Pre-Entrega
# Ejercicio 1: Crear un programa que permita agregar productos a una lista y mostrarlos en pantalla.
productos = []

while True:
    cartel_bienvenida = "bienvenido a la tienda de star wars".upper()
    print(cartel_bienvenida)
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        while True:
            nombre_producto = input("Ingrese el nombre del producto: ").strip()
            if nombre_producto == "":
                print("Debe agregar un producto.")
            else:
                break
        while True:
            cat_producto = (input("Ingrese su categoria: "))
            if cat_producto == "":
                print("Debe agregar una categoria.")
            else:
                break
        while True:
            precio_producto = (input("Ingrese su precio sin centavos: "))
            if precio_producto == "":
                print("Debe agregar un precio sin centavos.")
            else:
                break              
        productos.append({"nombre": nombre_producto.lower(), "categoria": cat_producto, "precio": precio_producto})
        lista_productos = productos
        
        print(f"El producto {nombre_producto.upper()}, de la categoria {cat_producto.upper()} fue agregado correctamente y su valor es de ${precio_producto}")
    elif opcion == 2:
        if not productos:
            print("No hay productos en la tienda.")
        else:
            for producto in productos:
                print(f"Nombre: {producto['nombre'].upper()}, categoria: {producto['categoria'].upper()}, precio: {producto['precio']}")
    elif opcion == 3:
        nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
        encontrado = False
        for producto in productos:
            if producto['nombre'] == nombre_buscar.lower():
                print(f"Producto encontrado: Nombre: {producto['nombre'].upper()}, categoria: {producto['categoria'].upper()}, precio: {producto['precio']}")
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
