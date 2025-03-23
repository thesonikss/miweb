class Perro:
    patas = 4  # se puede agregar propiedades tambien dentro de la misma clase

    def __init__(self, nombre):
        self.name = nombre

    def habla(self):
        print(f"{self.name} dice Guau!")


Perro.patas = 3
mi_perro = Perro("Huachimingo")
mi_perro.patas = 5
print(Perro.patas)
print(mi_perro.patas)
