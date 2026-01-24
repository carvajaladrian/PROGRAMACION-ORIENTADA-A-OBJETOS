class CitaMedica:
    #Clase que representa una cita médica.
    def __init__(self, paciente, doctor, fecha, hora):
        #Constructor: Se ejecuta automáticamente al crear el objeto Inicializa los datos de la cita médica.
        self.paciente = paciente
        self.doctor = doctor
        self.fecha = fecha
        self.hora = hora
        print(f"[INIT] Cita creada para {self.paciente} con el Dr. {self.doctor}")

    def mostrar_cita(self):
        #Muestra la información del cita.

        print("Cita:")
        print(f"Paciente: {self.paciente}")
        print(f"Doctor: {self.doctor}")
        print(f"Fecha: {self.fecha}")
        print(f"Hora: {self.hora}")

    def reprogramar(self, nueva_fecha, nueva_hora):
        #Permite cambiar la fecha y hora de la cita.

        self.fecha = nueva_fecha
        self.hora = nueva_hora
        print("[INFO] Cita reprogramada correctamente")

    def __del__(self):
        #Destructor: Se ejecuta cuando el objeto se elimina o el programa finaliza.

        print(f"[DEL] Cita médica de {self.paciente} cancelada o finalizada")

cita = CitaMedica(paciente="Adrian Carvajal", doctor="Carlos Mejia",fecha="2026-02-10",hora="09:30")
cita.mostrar_cita()
cita.reprogramar("2026-02-12", "11:00")
del cita
print("Fin del sistema de citas médicas")