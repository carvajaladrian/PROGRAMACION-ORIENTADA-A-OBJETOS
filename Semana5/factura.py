#El programa permite registrar un producto, calcular el subtotal, el IVA y el total a de una factura

# valor del IVA
IVA = 0.15
# Clase en CamelCase
class Factura:
    def __init__(self, nombre_producto, precio_unitario, cantidad):
        # Datos de la factura
        self.nombre_producto = nombre_producto    # string
        self.precio_unitario = precio_unitario    # float
        self.cantidad = cantidad                  # int
        self.factura_pagada = False               # boolean

    # Función en snake_case
    def calcular_subtotal(self):
        return self.precio_unitario * self.cantidad

    # Función en snake_case
    def calcular_iva(self):
        return self.calcular_subtotal() * IVA

    # Función en snake_case
    def calcular_total(self):
        return self.calcular_subtotal() + self.calcular_iva()

    def mostrar_factura(self):
        #Muestra los datos de la factura.
        print("\n--- FACTURA ---")
        print(f"Producto: {self.nombre_producto}")
        print(f"Precio unitario: {self.precio_unitario}")
        print(f"Cantidad: {self.cantidad}")
        print(f"Subtotal: {self.calcular_subtotal():.2f}")
        print(f"IVA (15%): {self.calcular_iva():.2f}")
        print(f"Total a pagar: {self.calcular_total():.2f}")
        print(f"Factura pagada: {self.factura_pagada}")

# Ingreso de datos
nombre_producto = input("Ingrese el nombre del producto: ")
precio_unitario = float(input("Ingrese el precio unitario: "))
cantidad = int(input("Ingrese la cantidad: "))

# Crear objeto Factura
mi_factura = Factura(nombre_producto, precio_unitario, cantidad)

# Mostrar la factura
mi_factura.mostrar_factura()