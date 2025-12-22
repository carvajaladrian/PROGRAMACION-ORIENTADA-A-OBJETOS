# ------------------ CLASE EQUIPO ------------------
class EquipoFutbol:
    """ Representa un equipo de fútbol.
    Usa encapsulamiento con atributos privados."""
    def __init__(self, nombre, categoria, jugadores):
        self.__nombre = nombre
        self.__categoria = categoria
        self.__jugadores = jugadores

    def mostrar_info(self):
        """Muestra la información del equipo."""
        print(f"Equipo: {self.__nombre} | Categoría: {self.__categoria} | Jugadores: {self.__jugadores}")

    def obtener_jugadores(self):
        """Devuelve la cantidad de jugadores."""
        return self.__jugadores
# ------------------ CLASE TORNEO ------------------
class TorneoFutbol:
    """Contiene los equipos inscritos en un torneo."""
    def __init__(self):
        self._equipos = []

    def inscribir_equipo(self, equipo):
        """Agrega un equipo al torneo."""
        if isinstance(equipo, EquipoFutbol):
            self._equipos.append(equipo)

    def mostrar_equipos(self):
        """Muestra los equipos inscritos."""
        print("\nEquipos inscritos:")
        for equipo in self._equipos:
            equipo.mostrar_info()
# ------------------ CLASE TORNEO DETALLADO ------------------
class TorneoFutbolDetallado(TorneoFutbol):
    """Hereda de TorneoFutbol y agrega un resumen final."""
    def mostrar_resumen(self):
        self.mostrar_equipos()
        total_jugadores = sum(e.obtener_jugadores() for e in self._equipos)
        print(f"\nTotal de equipos: {len(self._equipos)}")
        print(f"Total de jugadores inscritos: {total_jugadores}")

# ------------------ PROGRAMA PRINCIPAL ------------------
torneo = TorneoFutbolDetallado()
cantidad = int(input("Ingrese la cantidad de equipos a inscribir: "))

for i in range(cantidad):
    print(f"\nEquipo #{i + 1}")
    nombre = input("Nombre del equipo: ")
    categoria = input("Categoría: ")
    jugadores = int(input("Número de jugadores: "))
    torneo.inscribir_equipo(EquipoFutbol(nombre, categoria, jugadores))

print("\n===== RESUMEN DEL TORNEO =====")
torneo.mostrar_resumen()
