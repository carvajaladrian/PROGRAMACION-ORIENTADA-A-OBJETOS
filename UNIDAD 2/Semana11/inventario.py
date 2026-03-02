import json
from producto import Producto

class Inventario:
    def __init__(self):
        # Diccionario para búsqueda rápida por ID
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.get_id() in self.productos:
            print("El producto ya existe.")
        else:
            self.productos[producto.get_id()] = producto
            print("Producto agregado correctamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("Producto eliminado.")
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].set_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].set_precio(precio)
            print("Producto actualizado.")
        else:
            print("Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        encontrados = []
        for producto in self.productos.values():
            if nombre.lower() in producto.get_nombre().lower():
                encontrados.append(producto)

        return encontrados

    def mostrar_todos(self):
        if not self.productos:
            print("Inventario vacío.")
        else:
            for producto in self.productos.values():
                print(producto)

    # Guardar en archivo
    def guardar_en_archivo(self, nombre_archivo):
        with open(nombre_archivo, "w") as archivo:
            datos = {id_prod: prod.to_dict() for id_prod, prod in self.productos.items()}
            json.dump(datos, archivo, indent=4)
        print("Inventario guardado correctamente.")

    # Cargar desde archivo
    def cargar_desde_archivo(self, nombre_archivo):
        try:
            with open(nombre_archivo, "r") as archivo:
                datos = json.load(archivo)
                for id_prod, prod_data in datos.items():
                    self.productos[id_prod] = Producto.from_dict(prod_data)
            print("Inventario cargado correctamente.")
        except FileNotFoundError:
            print("No existe archivo previo. Se iniciará inventario vacío.")