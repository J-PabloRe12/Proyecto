from inicializador import cargar_inventario
from inicializador import guardar_inventario

def añadir_producto(inventario):
    #Acá se añaden los prodcutos
    nombre = input("Nombre del producto: ").lower().upper()
    cantidad = int(input("Cantidad disponible: "))
    precio = float(input("Precio unitario: "))
    inventario[nombre] = {'cantidad': cantidad, 'precio': precio}
    guardar_inventario(inventario)
    print(f"Producto '{nombre}' añadido.")


def actualizar_producto(inventario):
    #Se actualiza ya un articulo creado
    nombre = input("Nombre del producto a actualizar: ")
    if nombre in inventario:
        cantidad = int(input("Nueva cantidad disponible: "))
        precio = float(input("Nuevo precio unitario: "))
        inventario[nombre] = {'cantidad': cantidad, 'precio': precio}
        guardar_inventario(inventario)
        print(f"Producto '{nombre}' actualizado.")
    else:
        print(f"Producto '{nombre}' no encontrado.")


def eliminar_producto(inventario):
    """Elimina un producto del inventario."""
    nombre = input("Nombre del producto a eliminar: ")
    if nombre in inventario:
        del inventario[nombre]
        guardar_inventario(inventario)
        print(f"Producto '{nombre}' eliminado.")
    else:
        print(f"Producto '{nombre}' no encontrado.")


def mostrar_inventario(inventario):
    """Muestra todos los productos disponibles en el inventario."""
    if inventario:
        print("Inventario:")
        for nombre, datos in inventario.items():
            print(f"- {nombre}: Cantidad: {datos['cantidad']}, Precio: {datos['precio']}")
    else:
        print("El inventario está vacío.")


def menu():
    """Muestra el menú de opciones y ejecuta la acción seleccionada."""
    inventario = cargar_inventario()

    while True:
        print("\nMenú:")
        print("1. Añadir producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar productos")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            añadir_producto(inventario)
        elif opcion == '2':
            actualizar_producto(inventario)
        elif opcion == '3':
            eliminar_producto(inventario)
        elif opcion == '4':
            mostrar_inventario(inventario)
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, intente nuevamente.")


if __name__ == "__main__":
    menu()
