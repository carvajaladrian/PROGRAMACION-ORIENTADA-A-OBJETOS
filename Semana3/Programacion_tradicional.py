# Programación Orientada a Objetos (POO)
# Ejemplo: Gestión de la temperatura semanal

class Clima:
    def __init__(self, dias=7):
        self.temperaturas = []
        self.dias = dias

    def agregar_temperatura(self, valor):
        self.temperaturas.append(valor)

    def calcular_promedio(self):
        if len(self.temperaturas) == 0:
            return 0
        return sum(self.temperaturas) / len(self.temperaturas)

# Crear una instancia de la clase Clima
semana = Clima()

# Uso de los métodos en la programación orientada a objetos
semana.agregar_temperatura(22)
semana.agregar_temperatura(24)
semana.agregar_temperatura(23)
semana.agregar_temperatura(25)
semana.agregar_temperatura(21)
semana.agregar_temperatura(20)
semana.agregar_temperatura(23)

# Calcular el promedio semanal
promedio = semana.calcular_promedio()

# Imprimir resultados
print("Temperaturas registradas:", semana.temperaturas)
print("Promedio semanal:", promedio)
