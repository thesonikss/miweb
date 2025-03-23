class Animal:
    def comer(self):
        print("comiendo")


class Perro(Animal):  # aqui estamos heredando de la clase animal sus metodos
    def pasear(self):
        print("paseando")


class Chanchito(Perro):  # aqui estamos heredando de la clase perro, que contiene ya la herencia de la clase animal
    def programar(self):
        print("Chanchito Programando")


chanchito = Chanchito()
perro = Perro()
