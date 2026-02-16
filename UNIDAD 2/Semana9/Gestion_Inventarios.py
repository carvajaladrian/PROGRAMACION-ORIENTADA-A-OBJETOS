# ---------- CLASE PRODUCTO ----------
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self._id = id
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # GETTERS
    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    # SETTERS
    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def set_precio(self, precio):
        self._precio = precio

    def mostrar(self):
        print("ID:", self._id,
              "| Nombre:", self._nombre,
              "| Cantidad:", self._cantidad,
              "| Precio:", self._precio)


# ---------- CLASE INVENTARIO ----------
class Inventario:
    def __init__(self):
        self.lista_productos = []

    # Agregar producto (ID único)
    def agregar_producto(self):
        id = input("ID: ")

        # Verificar si el ID ya existe
        for p in self.lista_productos:
            if p.get_id() == id:
                print("Ese ID ya existe")
                return

        nombre = input("Nombre: ")
        cantidad = int(input("Cantidad: "))
        precio = float(input("Precio: "))

        nuevo = Producto(id, nombre, cantidad, precio)
        self.lista_productos.append(nuevo)
        print("Producto agregado")

    # Eliminar producto
    def eliminar_producto(self):
        id = input("ID a eliminar: ")
        for p in self.lista_productos:
            if p.get_id() == id:
                self.lista_productos.remove(p)
                print("Producto eliminado")
                return
        print("Producto no encontrado")

    # Actualizar producto
    def actualizar_producto(self):
        id = input("ID a actualizar: ")
        for p in self.lista_productos:
            if p.get_id() == id:
                nueva_cantidad = int(input("Nueva cantidad: "))
                nuevo_precio = float(input("Nuevo precio: "))
                p.set_cantidad(nueva_cantidad)
                p.set_precio(nuevo_precio)
                print("Producto actualizado")
                return
        print("Producto no encontrado")

    # Buscar por nombre
    def buscar_producto(self):
        nombre = input("Nombre a buscar: ")
        for p in self.lista_productos:
            if nombre.lower() in p.get_nombre().lower():
                p.mostrar()

    # Mostrar inventario
    def mostrar_inventario(self):
        if len(self.lista_productos) == 0:
            print("Inventario vacío")
        else:
            for p in self.lista_productos:
                p.mostrar()


# ---------- MENU ----------
inventario = Inventario()

while True:
    print("\n===== MENU =====")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto")
    print("5. Mostrar inventario")
    print("6. Salir")

    opcion = input("Seleccione opción: ")

    if opcion == "1":
        inventario.agregar_producto()
    elif opcion == "2":
        inventario.eliminar_producto()
    elif opcion == "3":
        inventario.actualizar_producto()
    elif opcion == "4":
        inventario.buscar_producto()
    elif opcion == "5":
        inventario.mostrar_inventario()
    elif opcion == "6":
        break
    else:
        print("Opción inválida")