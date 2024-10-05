import tkinter as tk

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")

        # Campo de entrada para nuevas tareas
        self.task_entry = tk.Entry(root)
        self.task_entry.pack()

        # Botones
        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack()
        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.pack()
        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack()

        # Lista de tareas
        self.task_list = tk.Listbox(root)
        self.task_list.pack()

        # Atajos de teclado
        self.root.bind("<Return>", self.add_task)

        # Inicializar la lista de tareas (opcional)
        self.tasks = []

    def add_task(self, event=None):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def complete_task(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            self.task_list.delete(selected_index)
            # Puedes agregar lógica aquí para marcar la tarea como completada en una base de datos o archivo, si lo deseas

    def delete_task(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            self.task_list.delete(selected_index)
            del self.tasks[selected_index[0]]

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()