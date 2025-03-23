usuarios = [["Chanchito", 13],
            ["Felipe", 17],
            ["Pulga", 8]]
nombres = list(map(lambda usuario: usuario[0], usuarios))
print(nombres)
# La funcion map Crea un iterador que calcule la función usando argumentos de cada uno de los iterables.
# Se detiene cuando se agota el iterable más corto.


# con la funcion filter le indicamos que es lo que vamos a hacer nosotros para dejar elementos dentro de este listado
# considerar que menosUsuarios va a ser una lista diferente a usuarios, por ello aplicamos la funcion list, estamos creando otra lista
# menosUsuarios = list(filter(lambda usuario: usuario[1] > 10, usuarios))
# # la funcion lambda que le estamos pasando a filter si evalua en true nos va a devolver el elemento
# print(menosUsuarios)
