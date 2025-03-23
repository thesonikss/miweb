class Perro:
    def __init__(self, nombre):
        self.nombre = nombre

    @property
    def nombre(self):
        print("Pasando por getter")
        return self.__nombre
# al agregar el decorador property automaticamente genera otro decorador
# con el nombre del metodo al que le agregamos el property

    @nombre.setter  # con el .setter le indicamos cual va a ser el setter
    def nombre(self, nombre):
        print("Pasando por setter")
        if nombre.strip():
            self.__nombre = nombre
        return


perro = Perro("Choclo")
print(perro.nombre)
