# lista = [1, 2, 3, 4, 5]
# print(*lista)
# lista_tupla = [12, 22, 32, 42, 52]
# print(lista_tupla)
# print(*lista_tupla)
# # lista_combinada = "Inicio" + lista +  lista_tupla + "final"  # esto no se puede hacer
# lista_combinada = ["Inicio", *lista, *lista_tupla, "final"]
# # cuando se le agrega *, se considera un iterable, de lo contrario entrega el listado como un objeto
# print(*lista_combinada)
punto1 = {"x": 19, "y": "hola"}
punto2 = {"y": 15}
nuevoPunto = {**punto1, **punto2, "z": "mundo"}
# se realiza el empaquetamiento de derecha a izquierda, por ende si tomo un valor ya en el diccionario
# ignorara el mismo para futuros diccionarios
print(nuevoPunto)
