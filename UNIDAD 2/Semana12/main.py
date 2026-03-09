from biblioteca import Biblioteca
from libro import Libro
from usuario import Usuario

biblioteca = Biblioteca()

while True:

    print("\n--- SISTEMA BIBLIOTECA DIGITAL ---")
    print("1. Agregar libro")
    print("2. Quitar libro")
    print("3. Registrar usuario")
    print("4. Eliminar usuario")
    print("5. Prestar libro")
    print("6. Devolver libro")
    print("7. Buscar libro")
    print("8. Listar libros prestados")
    print("9. Salir")

    opcion = input("Seleccione una opción: ")

    # AGREGAR LIBRO
    if opcion == "1":

        titulo = input("Título: ")
        autor = input("Autor: ")
        categoria = input("Categoría: ")
        isbn = input("ISBN: ")

        libro = Libro(titulo, autor, categoria, isbn)

        biblioteca.agregar_libro(libro)

    # QUITAR LIBRO
    elif opcion == "2":
        isbn = input("Ingrese ISBN del libro: ")
        biblioteca.quitar_libro(isbn)

    # REGISTRAR USUARIO
    elif opcion == "3":
        nombre = input("Nombre del usuario: ")
        id_usuario = input("ID del usuario: ")
        usuario = Usuario(nombre, id_usuario)
        biblioteca.registrar_usuario(usuario)

    # ELIMINAR USUARIO
    elif opcion == "4":
        id_usuario = input("Ingrese ID del usuario: ")
        biblioteca.eliminar_usuario(id_usuario)

    # PRESTAR LIBRO
    elif opcion == "5":

        id_usuario = input("ID del usuario: ")
        isbn = input("ISBN del libro: ")

        biblioteca.prestar_libro(id_usuario, isbn)

    # DEVOLVER LIBRO
    elif opcion == "6":

        id_usuario = input("ID del usuario: ")
        isbn = input("ISBN del libro: ")

        biblioteca.devolver_libro(id_usuario, isbn)

    # BUSCAR LIBRO
    elif opcion == "7":

        texto = input("Buscar por título, autor o categoría: ")
        biblioteca.buscar_libro(texto)

    # LISTAR LIBROS PRESTADOS
    elif opcion == "8":

        id_usuario = input("ID del usuario: ")
        biblioteca.listar_libros_prestados(id_usuario)

    # SALIR
    elif opcion == "9":

        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida")