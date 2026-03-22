import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
# Función para agregar evento
def agregar_evento():
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    descripcion = entry_descripcion.get()

    # Verificar que los campos no estén vacíos
    if fecha == "" or hora == "" or descripcion == "":
        messagebox.showwarning("Advertencia", "Debe llenar todos los campos")
        return

    # Insertar datos en la tabla
    tabla_eventos.insert("", "end", values=(fecha, hora, descripcion))

    # Limpiar campos
    entry_hora.delete(0, tk.END)
    entry_descripcion.delete(0, tk.END)


# Función para eliminar evento
def eliminar_evento():
    seleccionado = tabla_eventos.selection()

    if not seleccionado:
        messagebox.showwarning("Advertencia", "Seleccione un evento")
        return

    confirmacion = messagebox.askyesno("Confirmar", "¿Desea eliminar el evento?")

    if confirmacion:
        tabla_eventos.delete(seleccionado)


# Función para salir
def salir():
    ventana.quit()


# -----------------------------
# VENTANA PRINCIPAL
# -----------------------------

ventana = tk.Tk()
ventana.title("Agenda Personal")
ventana.geometry("600x400")

# -----------------------------
# FRAME LISTA DE EVENTOS
# -----------------------------

frame_lista = tk.Frame(ventana)
frame_lista.pack(pady=10)

# TreeView
tabla_eventos = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")

tabla_eventos.heading("Fecha", text="Fecha")
tabla_eventos.heading("Hora", text="Hora")
tabla_eventos.heading("Descripción", text="Descripción")

tabla_eventos.pack()

# -----------------------------
# FRAME ENTRADA DE DATOS
# -----------------------------

frame_datos = tk.Frame(ventana)
frame_datos.pack(pady=10)

# Fecha
label_fecha = tk.Label(frame_datos, text="Fecha:")
label_fecha.grid(row=0, column=0)

entry_fecha = DateEntry(frame_datos)
entry_fecha.grid(row=0, column=1)

# Hora
label_hora = tk.Label(frame_datos, text="Hora:")
label_hora.grid(row=1, column=0)

entry_hora = tk.Entry(frame_datos)
entry_hora.grid(row=1, column=1)

# Descripción
label_descripcion = tk.Label(frame_datos, text="Descripción:")
label_descripcion.grid(row=2, column=0)

entry_descripcion = tk.Entry(frame_datos, width=30)
entry_descripcion.grid(row=2, column=1)

# -----------------------------
# FRAME BOTONES
# -----------------------------

frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

boton_agregar = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento)
boton_agregar.grid(row=0, column=0, padx=5)

boton_eliminar = tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=eliminar_evento)
boton_eliminar.grid(row=0, column=1, padx=5)

boton_salir = tk.Button(frame_botones, text="Salir", command=salir)
boton_salir.grid(row=0, column=2, padx=5)

# -----------------------------
# EJECUTAR APLICACIÓN
# -----------------------------

ventana.mainloop()