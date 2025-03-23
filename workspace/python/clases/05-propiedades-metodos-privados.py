class Perro:

    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.__nombre} dice Guau!")

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    @classmethod
    def factory(cls):
        return cls("Chanchito Feliz", 4)


perro1 = Perro.factory()
perro1.habla()
perro1.set_nombre("guaje")
print(perro1.__dict__)
