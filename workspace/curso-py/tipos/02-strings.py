nombre_curso1 = 'Ultimate Python Simples'
nombre_curso2 = "Ultimate Python Dobles"
nombre_curso3 = """
Hola Mundo
Como
Están?
"""
print(nombre_curso1)
print(nombre_curso2)
print(nombre_curso3)
len(nombre_curso1)  # Entrega el largo del string
print(len(nombre_curso1))  # Imprimir el largo del string nombre_curso1
print(nombre_curso2[0])  # Imprime un caracter en especifico del string
# Nos entregara todos los char contenidos entre esas posiciones
print(nombre_curso1[0:8])
# Si no le asignamos un valor de inicio comenzara desde el primero
print(nombre_curso1[:8])
# Si no le asignamos un valor final entregará hasta el final del string
print(nombre_curso1[0:])
