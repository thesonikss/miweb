from abc import ABC, abstractmethod
# abc viene de abstract class, ABC es la clase de la cual vamos a querer heredar
# abstractmethods sirve para las propiedades y los metodos


class Model(ABC):

    def __init__(self):
        if not self.tabla:
            print("Error, tienes que definir una tabla")

    @property
    @abstractmethod
    def tabla(self):
        pass

    def guardar(self):
        print(f"Guardando {self.tabla} en BBDD")

    @classmethod
    def buscar_por_id(self, _id):
        print(f"buscando por id {_id} en la tabla {self.tabla}")


class Usuario(Model):
    tabla = "Usuario"


usuario = Usuario()
Usuario.buscar_por_id(123)
