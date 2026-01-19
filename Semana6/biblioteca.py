# Clase base
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo      # Atributo público
        self.autor = autor        # Atributo público
        self.__prestado = False   # Atributo privado (encapsulación)

    def prestar(self):
        if not self.__prestado:
            self.__prestado = True
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' ya está prestado.")

    def devolver(self):
        self.__prestado = False
        print(f"El libro '{self.titulo}' ha sido devuelto.")

    def estado(self):  # Método getter
        return self.__prestado

    def mostrar_info(self):
        #Este método será sobrescrito en la clase hija (polimorfismo)

        estado = "Prestado" if self.__prestado else "Disponible"
        print(f"Título: {self.titulo}, Autor: {self.autor}, Estado: {estado}")


# Clase derivada (herencia)
class LibroDigital(Libro):
    def __init__(self, titulo, autor, tamaño_mb):
        super().__init__(titulo, autor)  # Llama a la clase base
        self.tamaño_mb = tamaño_mb

    # Polimorfismo: método sobrescrito
    def mostrar_info(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}, Tamaño: {self.tamaño_mb} MB (Digital)")


# Programa principal
if __name__ == "__main__":
    # Creación de instancias
    libro_fisico = Libro("El Principito", "Antoine de Saint-Exupéry")
    libro_digital = LibroDigital("Python Básico", "Ana López", 4)

    # Uso de métodos
    libro_fisico.mostrar_info()
    libro_fisico.prestar()
    libro_fisico.mostrar_info()

    libro_digital.mostrar_info()  # Polimorfismo
