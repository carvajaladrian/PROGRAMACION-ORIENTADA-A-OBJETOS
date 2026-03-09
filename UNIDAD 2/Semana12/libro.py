class Libro:

    def __init__(self, titulo, autor, categoria, isbn):
        # Tupla para guardar titulo y autor (no cambiarán)
        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def obtener_titulo(self):
        return self.info[0]

    def obtener_autor(self):
        return self.info[1]

    def mostrar_info(self):
        print("Título:", self.info[0])
        print("Autor:", self.info[1])
        print("Categoría:", self.categoria)
        print("ISBN:", self.isbn)