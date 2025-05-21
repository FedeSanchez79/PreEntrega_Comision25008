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

    match opcion:
        
        case 1:
            salir = False
            while not salir:
                while True: # creo este bucle para cuando pregunte de agregar otro producto y responda que si vuelva al inicio
                        nombre_producto = input("Ingrese el nombre del producto: ").strip()
                        if nombre_producto == "":
                                print("Debe agregar un producto.")
                        else:
                            break
                        while True:
                            cat_producto = (input("Ingrese su categoria: "))
                            if cat_producto == "":
                                print("Debe agregar una categoria.")
                                print("Las categorias disponibles son: 'comic', 'coleccionables', 'sables de luz'")    
                            else:
                                break
                        while True:
                            precio_producto = int(input("Ingrese su precio sin centavos: "))
                            if precio_producto == "":
                                print("Debe agregar un precio sin centavos.")
                            else:
                                break              
                        productos.append({"nombre": nombre_producto.lower(), "categoria": cat_producto, "precio": precio_producto})
                        lista_productos = productos        
                        print(f"El producto {nombre_producto.upper()}, de la categoria {cat_producto.upper()} fue agregado correctamente y su valor es de ${precio_producto}")
                        while True:
                            nuevo_ingreso = input("¿Desea agregar otro producto? (SI/NO): ").lower()
                            if nuevo_ingreso == "si":
                                break 
                            elif nuevo_ingreso == "no":
                                salir = True
                                break
                            else:
                                print("Opción no válida, por favor responda con SI o NO.") 
                       
        case 2:
            if not productos:
                print("No hay productos en la tienda.")
            else:
                for i in range(len(productos)):
                    producto = productos[i]
                    print(f"{i+1}. Nombre: {producto['nombre'].upper()}, Categoría: {producto['categoria'].upper()}, Precio: {producto['precio']}")
            print("El total de productos en la tienda es de:", len(productos))        

        case 3:
            nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
            encontrado = False
            for producto in productos:
                if producto['nombre'] == nombre_buscar.lower():
                    print(f"Producto encontrado: Nombre: {producto['nombre'].upper()}, categoria: {producto['categoria'].upper()}, precio: {producto['precio']}")
                    print("Desea buscar algun otro producto?")
                    nueva_busqueda = input(("SI/NO: ") )
                    if nueva_busqueda.lower() == "si":
                        nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
                        encontrado = False
                    elif nueva_busqueda.lower() == "no":
                        continue
                    else:
                        print("Opción no válida, intente nuevamente.")
                        break
                    encontrado = True
                    break
            if not encontrado:
                print("Producto no encontrado.")
            print(nueva_busqueda)
        case 4:
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

        case 5:
            print("Gracias por usar la tienda. ¡Hasta luego!")
            break

        case _:
            print("Opción no válida, intente nuevamente.")

