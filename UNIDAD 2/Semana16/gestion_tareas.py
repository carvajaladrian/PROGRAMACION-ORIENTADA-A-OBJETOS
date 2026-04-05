import tkinter as tk
from tkinter import messagebox

class TaskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")

        # Lista de tareas (texto, estado)
        self.tasks = []

        # Campo de entrada
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)
        self.entry.focus()

        # Botones
        frame = tk.Frame(root)
        frame.pack()

        self.add_btn = tk.Button(frame, text="Añadir Tarea", command=self.add_task)
        self.add_btn.grid(row=0, column=0, padx=5)

        self.complete_btn = tk.Button(frame, text="Marcar Completada", command=self.complete_task)
        self.complete_btn.grid(row=0, column=1, padx=5)

        self.delete_btn = tk.Button(frame, text="Eliminar Tarea", command=self.delete_task)
        self.delete_btn.grid(row=0, column=2, padx=5)

        # Lista de tareas
        self.listbox = tk.Listbox(root, width=50, height=10)
        self.listbox.pack(pady=10)

        # Atajos de teclado
        self.root.bind("<Return>", lambda event: self.add_task())
        self.root.bind("<c>", lambda event: self.complete_task())
        self.root.bind("<C>", lambda event: self.complete_task())
        self.root.bind("<Delete>", lambda event: self.delete_task())
        self.root.bind("<d>", lambda event: self.delete_task())
        self.root.bind("<D>", lambda event: self.delete_task())
        self.root.bind("<Escape>", lambda event: self.root.quit())

    def add_task(self):
        task_text = self.entry.get().strip()
        if task_text:
            self.tasks.append((task_text, False))
            self.update_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "La tarea no puede estar vacía.")

    def complete_task(self):
        try:
            index = self.listbox.curselection()[0]
            text, _ = self.tasks[index]
            self.tasks[index] = (text, True)
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Aviso", "Selecciona una tarea.")

    def delete_task(self):
        try:
            index = self.listbox.curselection()[0]
            del self.tasks[index]
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Aviso", "Selecciona una tarea.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task, completed in self.tasks:
            display_text = f"✔ {task}" if completed else f"✗ {task}"
            self.listbox.insert(tk.END, display_text)

# Ejecutar
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskApp(root)
    root.mainloop()