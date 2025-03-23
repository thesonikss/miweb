# def suma(a, b):
#     print(a + b)
# suma(2, 5)
def suma(*numeros):
    # con el * antes del nombre le decimos que va a ser un iterable
    # permite que la funcion sea repetitiva, osea que se puede utilizar en un for
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(2, 5, 7)
suma(2, 5)
suma(2, 8, 7, 45, 32)
