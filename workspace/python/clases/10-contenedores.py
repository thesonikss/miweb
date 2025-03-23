class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Producto: {self.nombre} - Precio: {self.precio}"


class Categoria:
    productos = []

    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos

    def agregar(self, producto):
        self.productos.append(producto)

    def imprimir(self):
        for producto in self.productos:
            print(producto)


kayak = Producto("Kayak", 1500)
bicicleta = Producto("Bicicleta", 750)
surfboard = Producto("Surfboard", 500)
# aqui estamos creando directamente una lista
deportes = Categoria("Deportes", [])
deportes.agregar(surfboard)
deportes.agregar(kayak)
deportes.agregar(bicicleta)
deportes.imprimir()
