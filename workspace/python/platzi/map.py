# number = [1, 2, 3, 4, 5]
# number_v2 = []
# number_v2 = list(map(lambda x: x*2, number))
# print(number_v2)

number = [1, 2, 3, 4]
number_2 = [9, 8, 7, 6, 5]
suma_numeros = list(map(lambda n1, n2: n1+n2, number, number_2))
print(suma_numeros)
#para sumar listas