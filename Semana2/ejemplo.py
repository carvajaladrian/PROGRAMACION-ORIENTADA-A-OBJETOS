# ============================================
#     Clase base: Mascota
# ============================================

# --------------------------------------------
# 1. ABSTRACCIÓN (Aplicada en la clase Mascota)
# --------------------------------------------

class Mascota:
    def __init__(self, nombre, especie, edad, genero):
        # =====================================================
        # 2. ENCAPSULAMIENTO (Protección de los datos)
        # =====================================================
        self._nombre = nombre
        self._especie = especie
        self._edad = edad
        self._genero = genero

    # -------- MÉTODO DE ABSTRACCIÓN --------
    def mostrar_info(self):
        return f"{self._nombre} ({self._especie}, {self._genero}), {self._edad} años"

    # -------- MÉTODOS DE ENCAPSULAMIENTO --------
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nuevo_nombre):
        if len(nuevo_nombre) > 0:
            self._nombre = nuevo_nombre

    def get_edad(self):
        return self._edad

    def set_edad(self, nueva_edad):
        if nueva_edad > 0:
            self._edad = nueva_edad


# ============================================
#     HERENCIA: Perro y Gato
# ============================================

# ---------------------------------------------------------
# 3. HERENCIA (Perro y Gato heredan de Mascota)
# ---------------------------------------------------------

class Perro(Mascota):
    def __init__(self, nombre, edad, genero, raza):
        super().__init__(nombre, "Perro", edad, genero)
        self.raza = raza

    # ---------------------------------------------
    # 4. POLIMORFISMO: mostrar_info() redefinido
    # ---------------------------------------------
    def mostrar_info(self):
        return (f"Perro: {self._nombre} ({self._genero}), "
                f"{self._edad} años - Raza: {self.raza}")


class Gato(Mascota):
    def __init__(self, nombre, edad, genero, color):
        super().__init__(nombre, "Gato", edad, genero)
        self.color = color

    def mostrar_info(self):
        return (f"Gato: {self._nombre} ({self._genero}), "
                f"{self._edad} años - Color: {self.color}")


# ============================================
#     PROGRAMA PRINCIPAL (uso de las clases)
# ============================================

m1 = Mascota("Pelusa", "Conejo", 2, "F")
p1 = Perro("Max", 5, "M", "Labrador")
g1 = Gato("Luna", 3, "F", "Gris")

print(m1.mostrar_info())
print(p1.mostrar_info())  # polimorfismo
print(g1.mostrar_info())  # polimorfismo

# Usando encapsulación para modificar datos de forma controlada
m1.set_nombre("Pelusita")
m1.set_edad(3)
print(m1.mostrar_info())
