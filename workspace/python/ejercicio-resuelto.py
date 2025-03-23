print("""
Bienvenidos a la calculadora
Para salir escribir salir
Las operaciones son: suma, multi, div, y resta
""")
resultado = ""
while True:
    resultado = input("Ingrese número: ")
    if resultado.lower() == "salir":