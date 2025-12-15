# Programación Tradicional
# Promedio semanal de temperatura

# Definición de variables globales
temperaturas = []
dias = 7

# Función para ingresar las temperaturas diarias
def ingresar_temperatura(valor):
    global temperaturas
    temperaturas.append(valor)

# Función para calcular el promedio semanal
def calcular_promedio():
    global temperaturas
    if len(temperaturas) == 0:
        return 0
    return sum(temperaturas) / len(temperaturas)

# Uso de las funciones en la programación tradicional
ingresar_temperatura(22)
ingresar_temperatura(24)
ingresar_temperatura(23)
ingresar_temperatura(25)
ingresar_temperatura(21)
ingresar_temperatura(20)
ingresar_temperatura(23)

# Calcular el promedio semanal
promedio = calcular_promedio()

# Imprimir resultados
print("Temperaturas registradas:", temperaturas)
print("Promedio semanal:", promedio)
