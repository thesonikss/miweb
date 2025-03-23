class Perro:
    def __init__(self, nombre):
        self.name = nombre

    def habla(self):
        print(f"{self.name} dice Guau!")


mi_perro = Perro("Huachimingo")
# para esta instancia el self de cada metodo dentro de la clase seria mi_perro

mi_perro2 = Perro("Kira")
mi_perro.habla()
mi_perro2.habla()
