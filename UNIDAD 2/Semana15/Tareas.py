import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Lista de Tareas")
ventana.geometry("400x400")

def agregar_tarea(event=None):
    #Agrega una nueva tarea a la lista
    tarea = entrada_tarea.get()  # Obtener texto del Entry

    if tarea != "":
        lista_tareas.insert(tk.END, tarea)  # Agregar al Listbox
        entrada_tarea.delete(0, tk.END)  # Limpiar campo

def marcar_completada():
    #Marca la tarea seleccionada como completada
    try:
        indice = lista_tareas.curselection()[0]  # Obtener índice seleccionado
        tarea = lista_tareas.get(indice)

        # Cambiar texto para indicar que está completada
        lista_tareas.delete(indice)
        lista_tareas.insert(indice, "✔" + tarea)

        # Cambiar color
        lista_tareas.itemconfig(indice, fg="gray")
    except:
        print("Selecciona una tarea")

def eliminar_tarea():
    #Elimina la tarea seleccionada
    try:
        indice = lista_tareas.curselection()[0]
        lista_tareas.delete(indice)
    except:
        print("Selecciona una tarea")

def doble_click(event):
    #Evento opcional: marcar como completada con doble clic
    marcar_completada()

# INTERFAZ GRÁFICA

# Campo de entrada
entrada_tarea = tk.Entry(ventana, width=30)
entrada_tarea.pack(pady=10)

# Evento: presionar ENTER para agregar tarea
entrada_tarea.bind("<Return>", agregar_tarea)

# Botón agregar
btn_agregar = tk.Button(ventana, text="Añadir Tarea", command=agregar_tarea)
btn_agregar.pack(pady=5)

# Lista de tareas
lista_tareas = tk.Listbox(ventana, width=40, height=10)
lista_tareas.pack(pady=10)

# Evento opcional: doble clic
lista_tareas.bind("<Double-Button-1>", doble_click)

# Botón completar
btn_completar = tk.Button(ventana, text="Marcar como Completada", command=marcar_completada)
btn_completar.pack(pady=5)

# Botón eliminar
btn_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=eliminar_tarea)
btn_eliminar.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()