# Pre-Entrega
# Ejercicio 1: Crear un programa que permita agregar productos a una lista y mostrarlos en pantalla.

# lista vacia para almacenar los productos
productos = []

# bucle para mostrar el cartel de bienvenida y las opciones
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
            # creo este bucle para cuando pregunte de agregar otro producto y responda que si vuelva al inicio
            while True: 
                # ingreso el nombre del producto sin importar el dato que ingrese
                while True: 
                    nombre_producto = input("Ingrese el nombre del producto: ").strip()
                    if nombre_producto == "":
                            print("Debe agregar un producto.")
                    else:
                        break
                # ingreso la categoria del producto y si no es valida vuelve a preguntar    
                while True: 
                    cat_producto = (input("Ingrese su categoria (COMIC/COLECCIONABLE/SABLE DE LUZ): "))
                    categorias = ("comic", "coleccionable", "sable de luz")
                    if cat_producto == "":
                        print("Debe agregar una categoria válida.")
                        print("Las categorias disponibles son: 'COMIC', 'COLECCIONABLE', 'SABLES DE LUZ'")  
                    elif cat_producto.lower() not in categorias:
                        print("Categoria no válida, por favor elija entre 'COMIC', 'COLECCIONABLE' o 'SABLE DE LUZ'.")  
                    else:
                        break
                # ingreso el precio del producto y si no es valido vuelve a preguntar    
                while True: 
                    precio_producto = int(input("Ingrese su precio sin centavos: "))
                    if precio_producto == "":
                        print("Debe agregar un precio sin centavos.")
                    elif not precio_producto:
                        print("Debe ingresar solo números enteros positivos (sin centavos, letras o símbolos).")
                    else:
                        precio_producto = int(precio_producto)
                    break
                # muestro el producto ingresado            
                productos.append({"nombre": nombre_producto.lower(), "categoria": cat_producto, "precio": precio_producto})
                lista_productos = productos        
                print(f"El producto {nombre_producto.upper()}, de la categoria {cat_producto.upper()} fue agregado correctamente y su valor es de ${precio_producto}")
                # creo un bucle para ver si desea agregar otro producto
                while True:
                    nuevo_ingreso = input("¿Desea agregar otro producto? (SI/NO): ").lower()
                    if nuevo_ingreso == "si":
                        break 
                    elif nuevo_ingreso == "no":
                        salir = True
                        break
                    else:
                        print("Opción no válida, por favor responda con SI o NO.") 
                break       
        case 2:
            # condicional por si no hay productos agregados
            if not productos:
                print("No hay productos en la tienda.")
            else:
                # muestro los productos ingresados
                for i in range(len(productos)):
                    producto = productos[i]
                    print(f"{i+1}. Nombre: {producto['nombre'].upper()}, Categoría: {producto['categoria'].upper()}, Precio: {producto['precio']}")
            print("El total de productos en la tienda es de:", len(productos))        

        case 3:
            # creo una variable para acceder al nombre del producto a buscar
            nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
            encontrado = False
            # creo un bucle para que de la opcion de buscar otro producto            
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
            # condicional por si no encuentra el producto    
            if not encontrado:
                print("Producto no encontrado.")
            print(nueva_busqueda)
        case 4:
            # muestro los productos ingresados
            for i in range(len(productos)):
                producto = productos[i]
                print(f"{i+1}. Nombre: {producto['nombre'].upper()}, Categoría: {producto['categoria'].upper()}, Precio: {producto['precio']}")
            # creo una variable para acceder al nombre del producto a eliminar
            # Pedir el número del producto a eliminar
            indice = int(input("Ingrese el número del producto que desea eliminar: "))
            if 1 <= indice <= len(productos):
                eliminado = productos.pop(indice - 1)
                print(f"Producto {eliminado['nombre'].upper()} eliminado correctamente.")
            else:
                print("Número inválido. No existe un producto con ese número.")
            if not productos:
                print("No hay productos para eliminar.")

        case 5: 
            # salgo del bucle
            print("Gracias por usar la tienda. ¡Hasta luego!")
            break

        case _:
            print("Opción no válida, intente nuevamente.")

