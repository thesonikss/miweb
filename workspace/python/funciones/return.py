def suma(a, b):
    resultado = a+b
    return resultado


# la funcion return nos devuelve una variable desde la funcion
# luego se escribe en c gracias a la funcion return
c = suma(7, 2)
# una vez tiene un valor asignado la variable c, se ejecuta la funcion suma nuevamente
# cuando se ejecuta la funcion suma y se toma el resultado con return, esta se escribe en d
d = suma(c, 5)

print(c)
