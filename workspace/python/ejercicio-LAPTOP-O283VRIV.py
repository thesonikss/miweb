print("""
Bienvenidos a la calculadora
Para salir escribir salir
Las operaciones son: suma, multi, div, y resta
""")
operacion = ""
numero1 = ""
resultado = ""
resultado = input("Ingresar numero")
resultado = int(resultado)
while True:
    operacion = input("Ingrese Operacion")
    if operacion == "salir":
        break
    elif operacion == "suma":
        numero1 = input("Ingrese otro numero")
        numero1 = int(numero1)
        resultado += numero1
        print(resultado)
    elif operacion == "resta":
        numero1 = input("Ingrese otro numero")
        numero1 = int(numero1)
        resultado -= numero1
        print(resultado)
    elif operacion == "div":
        numero1 = input("Ingrese otro numero")
        numero1 = int(numero1)
        resultado /= numero1
        print(resultado)
    elif operacion == "multi":
        numero1 = input("Ingrese otro numero")
        numero1 = int(numero1)
        resultado *= numero1
        print(resultado)
    else:
        print("Ingrese una operacion valida")
