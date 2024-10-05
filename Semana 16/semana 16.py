import tkinter as tk
from tkinter import messagebox, Listbox, Scrollbar, END, StringVar


class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")

        # Variable para almacenar las tareas
        self.tasks = []

        # Configurar la interfaz gráfica
        self.setup_ui()

    def setup_ui(self):
        # Campo de entrada para nuevas tareas
        self.task_entry = tk.Entry(self.root, width=50)
        self.task_entry.pack(pady=10)

        # Botón para añadir tarea
        add_task_button = tk.Button(self.root, text="Añadir Tarea", command=self.add_task)
        add_task_button.pack(pady=5)

        # Botón para marcar tarea como completada
        complete_task_button = tk.Button(self.root, text="Marcar como Completada", command=self.complete_task)
        complete_task_button.pack(pady=5)

        # Botón para eliminar tarea
        delete_task_button = tk.Button(self.root, text="Eliminar Tarea", command=self.delete_task)
        delete_task_button.pack(pady=5)

        # Configurar lista de tareas
        self.task_listbox = Listbox(self.root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        # Scrollbar
        scrollbar = Scrollbar(self.root)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.task_listbox.yview)

        # Configuración de atajos de teclado
        self.root.bind('<Return>', lambda event: self.add_task())  # Enter
        self.root.bind('<c>', lambda event: self.complete_task())  # Tecla C
        self.root.bind('<Delete>', lambda event: self.delete_task())  # Tecla Delete
        self.root.bind('<Escape>', lambda event: self.root.quit())  # Escape

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, END)  # Limpiar el campo de entrada
        else:
            messagebox.showwarning("Advertencia", "Por favor ingresa una tarea.")

    def complete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            completed_task = self.tasks[selected_index]
            self.tasks[selected_index] = f"{completed_task} (Completada)"
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor selecciona una tarea.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_index)
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor selecciona una tarea.")

    def update_task_list(self):
        self.task_listbox.delete(0, END)  # Limpiar la lista de tareas
        for task in self.tasks:
            self.task_listbox.insert(END, task)


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
