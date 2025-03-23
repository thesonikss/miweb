class Ave:
    def __init__(self):
        self.volador = "Volador"

    def vuela(self):
        print("vuela ave")


class Pato(Ave):
    def __init__(self):
        super().__init__()
        self.nadar = "Nadador"

    def vuela(self):
        print("vuela pato")
        super().vuela()


pato = Pato()
print(pato.volador, pato.nadar)
