buscar = 10
for numero in range(7):
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break
# La palabra reservada break se utiliza para romper la ejecucion del for.
else:
    print("No encontre el numero buscado")
# En caso de que no se encuentre lo buscado se puede utilizar el else para dar una alternativa a la ejecucion
for char in "Ultimate Python":
    print(char)
