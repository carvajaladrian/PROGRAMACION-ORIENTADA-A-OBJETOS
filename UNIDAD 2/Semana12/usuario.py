class Usuario:

    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario

        # lista para libros prestados
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, isbn):

        for libro in self.libros_prestados:

            if libro.isbn == isbn:
                self.libros_prestados.remove(libro)
                return libro

        return None

    def mostrar_libros(self):

        if len(self.libros_prestados) == 0:
            print("No tiene libros prestados")

        else:
            for libro in self.libros_prestados:
                libro.mostrar_info()
                print("-----------")