import tkinter as tk

def agregar_nombre():
    nombre = entrada.get()
    lista_nombres.insert(tk.END, nombre)
    entrada.delete(0, tk.END)

def limpiar_lista():
    lista_nombres.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi Lista de Nombres")

# Crear los componentes
etiqueta = tk.Label(ventana, text="Ingrese un nombre:")
etiqueta.pack()

entrada = tk.Entry(ventana)
entrada.pack()

boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_nombre)
boton_agregar.pack()

lista_nombres = tk.Listbox(ventana)
lista_nombres.pack()

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
boton_limpiar.pack()

# Iniciar el bucle principal de la aplicación
ventana.mainloop()