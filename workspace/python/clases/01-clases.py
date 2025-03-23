class Perro:  # En las clases se escribe la primera letra de cada palabra en mayus
    # se debe usar la convencion con la primera letra en mayuscula como ej: MiPerro, LaCasa, etc
    def habla(self):
        print("Guau!")


mi_perro = Perro()
mi_perro.habla()


# Se le deben pasar dos argumentos, el objeto y la clase
print(isinstance(mi_perro, Perro))
print(isinstance(mi_perro, str))
