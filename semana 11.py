import json

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def obtener_info(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

class Inventario:
    def __init__(self):
        self.productos = {}

    def añadir_producto(self, producto):
        self.productos[producto.id] = producto

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            if cantidad is not None:
                self.productos[id].cantidad = cantidad
            if precio is not None:
                self.productos[id].precio = precio

    def buscar_producto(self, nombre):
        return [producto for producto in self.productos.values() if nombre in producto.nombre]

    def mostrar_productos(self):
        for producto in self.productos.values():
            print(producto.obtener_info())

    def guardar_inventario(self, archivo):
        with open(archivo, 'w') as f:
            json.dump(self.productos, f, default=lambda p: p.__dict__)
    def cargar_inventario(self, archivo):
        with open(archivo, 'r') as f:
            productos_data = json.load(f)
            for id, data in productos_data.items():
                self.añadir_producto(Producto(**data))

# Ejemplo de uso
inventario = Inventario()
inventario.añadir_producto(Producto(1, "Manzana", 50, 0.5))
inventario.mostrar_productos()
inventario.guardar_inventario('inventario.json')
