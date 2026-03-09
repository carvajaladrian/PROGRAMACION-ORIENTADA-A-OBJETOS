from libro import Libro
from usuario import Usuario

class Biblioteca:
    def __init__(self):
        # diccionario de libros disponibles
        self.libros = {}
        # diccionario de usuarios
        self.usuarios = {}
        # conjunto para ids únicos
        self.ids_usuarios = set()

    # AÑADIR LIBROS
    def agregar_libro(self, libro):
        self.libros[libro.isbn] = libro
        print("Libro agregado correctamente")

    # QUITAR LIBROS
    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado")
        else:
            print("Libro no encontrado")

    # REGISTRAR USUARIO
    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids_usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print("Usuario registrado correctamente")
        else:
            print("El ID ya existe")

    # DAR DE BAJA USUARIO
    def eliminar_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print("Usuario eliminado")
        else:
            print("Usuario no encontrado")

    # PRESTAR LIBRO
    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[id_usuario]
            libro = self.libros.pop(isbn)
            usuario.prestar_libro(libro)
            print("Libro prestado correctamente")
        else:
            print("No se pudo prestar el libro")

    # DEVOLVER LIBRO
    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            libro = usuario.devolver_libro(isbn)
            if libro:
                self.libros[isbn] = libro
                print("Libro devuelto correctamente")
            else:
                print("Ese libro no está prestado al usuario")

    # BUSCAR LIBRO
    def buscar_libro(self, texto):
        encontrado = False
        for libro in self.libros.values():
            if (texto.lower() in libro.obtener_titulo().lower() or
                texto.lower() in libro.obtener_autor().lower() or
                texto.lower() in libro.categoria.lower()):
                libro.mostrar_info()
                print("------")
                encontrado = True

        if not encontrado:
            print("No se encontraron libros")

    # LISTAR LIBROS PRESTADOS
    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            print("Libros prestados a:", usuario.nombre)
            usuario.mostrar_libros()
        else:
            print("Usuario no encontrado")