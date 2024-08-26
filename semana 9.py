class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto  # ID único
        self.nombre = nombre              # Nombre del producto
        self.cantidad = cantidad          # Cantidad disponible
        self.precio = precio              # Precio del producto

    # Getters
    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Setters
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

class Inventario:
    def __init__(self):
        self.productos = []  # Lista de productos

    def añadir_producto(self, producto):
        # Asegurarse de que el ID sea único
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: El ID ya existe.")
                return
        self.productos.append(producto)

    def eliminar_producto(self, id_producto):
        self.productos = [p for p in self.productos if p.get_id() != id_producto]

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                return
        print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        return resultados

    def mostrar_productos(self):
        for p in self.productos:
            print(f"ID: {p.get_id()}, Nombre: {p.get_nombre()}, Cantidad: {p.get_cantidad()}, Precio: {p.get_precio()}")

# Crear el inventario
inventario = Inventario()

# Añadir productos
producto1 = Producto(1, "Manzana", 50, 0.5)
producto2 = Producto(2, "Banana", 30, 0.3)
inventario.añadir_producto(producto1)
inventario.añadir_producto(producto2)

# Mostrar productos
inventario.mostrar_productos()

# Actualizar un producto
inventario.actualizar_producto(1, cantidad=60)

# Buscar productos
resultados = inventario.buscar_producto("manzana")
for p in resultados:
    print(f"Encontrado: {p.get_nombre()}")

# Eliminar un producto
inventario.eliminar_producto(2)

# Mostrar productos después de la eliminación
inventario.mostrar_productos()
