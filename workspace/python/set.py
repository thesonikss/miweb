# set significa grupo o conjunto
# es una coleccion de datos que no se pueden repetir y que tampoco estan ordenadas
primer = {1, 1, 2, 3, 4, 2}

primer.add(6)
primer.remove(1)
# print(primer)
segundo = [11, 12, 26, 4, 2]
segundo = set(segundo)

print(primer | segundo)
# el operador | se le llama union

print(primer & segundo)
# el & realiza una interseccion de los parametros existentes en ambos set

print(primer - segundo)
# el  operador - nos entrega la diferencia que existe entre ambos sets

print(primer ^ segundo)
# elimina los que se encuentran duplicados y entrega el resto

# los sets no se encuentran ordenados y tampoco se puede acceder a un elemento de estos
