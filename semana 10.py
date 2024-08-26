class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id_producto(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

    def to_file_format(self):
        return f"{self.id_producto},{self.nombre},{self.cantidad},{self.precio}"

import os

class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    def añadir_producto(self, producto):
        if producto.get_id_producto() in self.productos:
            print("Error: El ID del producto ya existe.")
        else:
            self.productos[producto.get_id_producto()] = producto
            self.guardar_inventario()
            print("Producto añadido exitosamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_inventario()
            print("Producto eliminado exitosamente.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
            self.guardar_inventario()
            print("Producto actualizado exitosamente.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        encontrados = [producto for producto in self.productos.values() if nombre.lower() in producto.get_nombre().lower()]
        if encontrados:
            for producto in encontrados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")

    def cargar_inventario(self):
        if not os.path.exists(self.archivo):
            print("Archivo de inventario no encontrado, se creará uno nuevo.")
            return

        try:
            with open(self.archivo, 'r') as file:
                for line in file:
                    id_producto, nombre, cantidad, precio = line.strip().split(',')
                    producto = Producto(int(id_producto), nombre, int(cantidad), float(precio))
                    self.productos[int(id_producto)] = producto
        except FileNotFoundError:
            print("Error: El archivo de inventario no se encontró.")
        except PermissionError:
            print("Error: No se tiene permiso para leer el archivo de inventario.")
        except Exception as e:
            print(f"Error al cargar el inventario: {e}")

    def guardar_inventario(self):
        try:
            with open(self.archivo, 'w') as file:
                for producto in self.productos.values():
                    file.write(producto.to_file_format() + '\n')
        except PermissionError:
            print("Error: No se tiene permiso para escribir en el archivo de inventario.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

# Crear una instancia de Inventario
inventario = Inventario()

# Añadir productos al inventario
producto1 = Producto(1, "Laptop", 10, 999.99)
producto2 = Producto(2, "Mouse", 50, 19.99)
producto3 = Producto(3, "Teclado", 30, 49.99)

inventario.añadir_producto(producto1)
inventario.añadir_producto(producto2)
inventario.añadir_producto(producto3)

# Mostrar todos los productos
print("Todos los productos:")
inventario.mostrar_productos()

# Buscar productos por nombre
print("\nBuscar productos con nombre 'Mouse':")
inventario.buscar_producto("Mouse")

# Actualizar producto
inventario.actualizar_producto(1, cantidad=8, precio=899.99)

# Mostrar todos los productos después de la actualización
print("\nTodos los productos después de la actualización:")
inventario.mostrar_productos()

# Eliminar un producto
inventario.eliminar_producto(2)

# Mostrar todos los productos después de la eliminación
print("\nTodos los productos después de la eliminación:")
inventario.mostrar_productos()
