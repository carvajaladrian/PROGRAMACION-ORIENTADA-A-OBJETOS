import tkinter as tk
from tkinter import ttk

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Lista de Víveres")
ventana.geometry("500x500")

# -------- FUNCIONES --------

# Función para agregar datos a la tabla
def agregar():
    cantidad = entrada_cantidad.get()
    viver = entrada_viver.get()

    if cantidad != "" and viver != "":
        tabla.insert("", "end", values=(cantidad, viver))
        entrada_cantidad.delete(0, tk.END)
        entrada_viver.delete(0, tk.END)

# Función para limpiar la tabla
def limpiar():
    for item in tabla.get_children():
        tabla.delete(item)

# -------- INTERFAZ --------

# Etiqueta cantidad
label_cantidad = tk.Label(ventana, text="Cantidad:")
label_cantidad.grid(row=0, column=0, padx=10, pady=10)

# Campo texto cantidad
entrada_cantidad = tk.Entry(ventana)
entrada_cantidad.grid(row=0, column=1)

# Etiqueta viver
label_viver = tk.Label(ventana, text="Vívere:")
label_viver.grid(row=1, column=0, padx=10, pady=10)

# Campo texto viver
entrada_viver = tk.Entry(ventana)
entrada_viver.grid(row=1, column=1)

# Botón agregar
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar)
boton_agregar.grid(row=2, column=0, pady=10)

# Botón limpiar
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
boton_limpiar.grid(row=2, column=1)

# -------- TABLA --------

tabla = ttk.Treeview(ventana, columns=("Cantidad", "Vívere"), show="headings")

tabla.heading("Cantidad", text="Cantidad")
tabla.heading("Vívere", text="Vívere")

tabla.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Ejecutar programa
ventana.mainloop()