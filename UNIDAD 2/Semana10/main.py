# main.py

from inventario import Inventario


def mostrar_menu():
    print("\n===== SISTEMA DE INVENTARIO =====")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto")
    print("5. Mostrar inventario")
    print("6. Salir")


def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                id = input("ID: ")
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                inventario.agregar_producto(id, nombre, cantidad, precio)

            elif opcion == "2":
                id = input("ID a eliminar: ")
                inventario.eliminar_producto(id)

            elif opcion == "3":
                id = input("ID a actualizar: ")
                cantidad = int(input("Nueva cantidad: "))
                precio = float(input("Nuevo precio: "))
                inventario.actualizar_producto(id, cantidad, precio)

            elif opcion == "4":
                nombre = input("Nombre a buscar: ")
                resultados = inventario.buscar_producto(nombre)
                if resultados:
                    for p in resultados:
                        p.mostrar()
                else:
                    print("Producto no encontrado.")

            elif opcion == "5":
                inventario.mostrar_inventario()

            elif opcion == "6":
                print("Saliendo del sistema...")
                break

            else:
                print("Opción inválida.")

        except ValueError:
            print("Error: Cantidad debe ser entero y precio decimal válido.")
        except Exception as e:
            print("Error inesperado:", e)


if __name__ == "__main__":
    main()