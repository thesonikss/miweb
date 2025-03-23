print("""
Bienvenidos a la calculadora
Para salir escribir salir
Las operaciones son: suma, multi, div, y resta
""")
numero = 0
resultado = 0
operacion = "calculadora"
resultado = input("Ingrese numero: ")
numero = int(numero)
resultado = int(resultado)
while operacion != "salir":
    operacion = input(f"Ingrese Operación: ")
    numero = input(f"Ingrese número: ")
    numero = int(numero)
    resultado = int(resultado)
    if operacion == "suma":
        resultado += numero
        print(resultado)
    if operacion == "resta":
        resultado -= numero
        print(resultado)
    if operacion == "multi":
        resultado *= numero
        print(resultado)
    if operacion == "div":
        resultado /= numero
        print(resultado)
