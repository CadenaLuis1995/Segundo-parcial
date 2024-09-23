import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

# Clase principal de la aplicación
class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda de Eventos")
        self.root.geometry("600x400")

        # Frame para la lista de eventos
        frame_lista = tk.Frame(self.root)
        frame_lista.pack(pady=10, padx=10, fill="both", expand=True)

        # Definir el Treeview para mostrar los eventos
        self.tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack(fill="both", expand=True)

        # Frame para los campos de entrada
        frame_entrada = tk.Frame(self.root)
        frame_entrada.pack(pady=10, padx=10, fill="x")

        # Etiquetas y campos de entrada
        tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
        self.date_entry = DateEntry(frame_entrada, date_pattern='y-mm-dd')
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_entrada, text="Hora:").grid(row=1, column=0, padx=5, pady=5)
        self.time_entry = tk.Entry(frame_entrada)
        self.time_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame_entrada, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
        self.desc_entry = tk.Entry(frame_entrada, width=40)
        self.desc_entry.grid(row=2, column=1, padx=5, pady=5)

        # Frame para los botones
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=10)

        # Botones
        tk.Button(frame_botones, text="Agregar Evento", command=self.agregar_evento).pack(side=tk.LEFT, padx=10)
        tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento).pack(side=tk.LEFT, padx=10)
        tk.Button(frame_botones, text="Salir", command=self.root.quit).pack(side=tk.LEFT, padx=10)

    # Función para agregar un evento
    def agregar_evento(self):
        fecha = self.date_entry.get()
        hora = self.time_entry.get()
        descripcion = self.desc_entry.get()

        if not (fecha and hora and descripcion):
            messagebox.showwarning("Campos Vacíos", "Por favor, complete todos los campos.")
            return

        # Agregar el evento a la lista (Treeview)
        self.tree.insert("", "end", values=(fecha, hora, descripcion))

        # Limpiar los campos de entrada
        self.time_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)

    # Función para eliminar un evento seleccionado
    def eliminar_evento(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Selección Vacía", "Por favor, seleccione un evento para eliminar.")
            return

        # Confirmación para eliminar el evento seleccionado
        confirmar = messagebox.askyesno("Eliminar Evento", "¿Está seguro de que desea eliminar el evento seleccionado?")
        if confirmar:
            self.tree.delete(selected_item)

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
