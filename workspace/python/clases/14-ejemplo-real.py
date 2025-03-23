class Model():
    tabla = False

    def __init__(self):
        if not self.tabla:  # pregunta si no se le ha asignado un valor a la tabla
            print("Error, tienes que definir una tabla")

    def guardar(self):
        print(f"Guardando {self.tabla} en BBDD")

    @classmethod
    def buscar_por_id(self, _id):
        print(f"buscando por {_id} en la tabla {self.tabla}")


class Usuario(Model):
    tabla = "Usuario"


usuario = Usuario()
usuario.guardar()
usuario.buscar_por_id(123)
