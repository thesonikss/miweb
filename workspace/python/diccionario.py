# los diccionarios son una coleccion de datos
# solo permiten asignar strings, esto se agrega a la izq
# su definiciom que va a la derecha puede ser cualquier cosa
# se le llaman llaves a las variables que agregamos a un diccionario
# estas tienen que ser si o si strings
punto = {"x": 25, "y": 50
         }
# j

# Esta es una forma de obtener lo que existe en el dicc sin que la app explote
# te entregara el valor de la llave si existe y de lo contrario devolvera "None"
# j

# si la llave no existe podemos pasarle un valor de esta forma
# aunque esto no agrega la llave al diccionario
# print(punto.get("zy", 55))


# del punto["x"]
# del (punto["y"])
# print(punto)

# for valor in punto:
#     print(valor, punto[valor])

# for valor in punto.items():
#     print(valor)

# for llave, valor in punto.items():
#     print(llave, valor)


# Ahora un ejemplo de como aplicar los diccionarios en un contexto real
# cuando trabajamos con elementos que vienen de una base de datos necesariamente deben tener un id unico
usuarios = [
    {"id": 1, "nombre": "Pablo"},
    {"id": 2, "nombre": "Maxito"},
    {"id": 3, "nombre": "Danilo"},
    {"id": 4, "nombre": "Daniel"},
]
for usuario in usuarios:
    print(usuario["id"], usuario["nombre"])
