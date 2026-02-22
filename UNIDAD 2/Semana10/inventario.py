import os
from producto import Producto
class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.lista_productos = []
        self.cargar_desde_archivo()

    # -------- CARGAR DESDE TXT --------
    def cargar_desde_archivo(self):
        try:
            if not os.path.exists(self.archivo):
                # Crear archivo si no existe
                with open(self.archivo, "w") as f:
                    pass
                print("Archivo inventario.txt creado.")
                return

            with open(self.archivo, "r") as f:
                for linea in f:
                    try:
                        datos = linea.strip().split(",")
                        id = datos[0]
                        nombre = datos[1]
                        cantidad = int(datos[2])
                        precio = float(datos[3])

                        producto = Producto(id, nombre, cantidad, precio)
                        self.lista_productos.append(producto)

                    except ValueError:
                        print("Línea con datos incorrectos ignorada.")

            print("Inventario cargado correctamente.")

        except FileNotFoundError:
            print("Error: El archivo no fue encontrado.")
        except PermissionError:
            print("Error: No tienes permisos para leer el archivo.")
        except Exception as e:
            print("Error inesperado al cargar:", e)

    # -------- GUARDAR EN TXT --------
    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w") as f:
                for p in self.lista_productos:
                    linea = f"{p.get_id()},{p.get_nombre()},{p.get_cantidad()},{p.get_precio()}\n"
                    f.write(linea)

            print("Archivo actualizado correctamente.")

        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo.")
        except Exception as e:
            print("Error inesperado al guardar:", e)

    # -------- OPERACIONES --------
    def agregar_producto(self, id, nombre, cantidad, precio):
        for p in self.lista_productos:
            if p.get_id() == id:
                print("El ID ya existe.")
                return

        nuevo = Producto(id, nombre, cantidad, precio)
        self.lista_productos.append(nuevo)
        self.guardar_en_archivo()
        print("Producto agregado y guardado en el archivo.")

    def eliminar_producto(self, id):
        for p in self.lista_productos:
            if p.get_id() == id:
                self.lista_productos.remove(p)
                self.guardar_en_archivo()
                print("Producto eliminado y archivo actualizado.")
                return

        print("Producto no encontrado.")

    def actualizar_producto(self, id, cantidad, precio):
        for p in self.lista_productos:
            if p.get_id() == id:
                p.set_cantidad(cantidad)
                p.set_precio(precio)
                self.guardar_en_archivo()
                print("Producto actualizado en el archivo.")
                return

        print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        encontrados = []
        for p in self.lista_productos:
            if nombre.lower() in p.get_nombre().lower():
                encontrados.append(p)
        return encontrados

    def mostrar_inventario(self):
        if len(self.lista_productos) == 0:
            print("Inventario vacío.")
        else:
            for p in self.lista_productos:
                p.mostrar()