gas = True
encendido = False
edad = 18
if gas and (encendido or edad > 17):
    # se necesita agregar el parentesis, sino vs code no sabe cual ejecutar primero
    # va a ejecutar primer el codigo contenido dentro del parentesis
    print("Puedes Avanzar")
else:
    print("Detente")
