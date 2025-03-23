pila = []
pila.append(1)
pila.append(2)
pila.append(3)
print(pila)
ultimoElemento = pila.pop()  # Nos retorna el ultimo elemento del listado, lo borra
print(ultimoElemento)
print(pila)
# Si se fija en este caso se trata de un listado, pero lo estamos trabajando como pila
# para trabajarlo como pila solo se utilizan los metodos append y pop
# se puede acceder al ultimo elemento de la lista indicandole el -1
print(pila[-1])

if not pila:  # esto es para realizar una comprobacion de si se encuentra vacia la pila
    print("pila vacia")
