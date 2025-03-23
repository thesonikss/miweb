animal = "   chanchito FELIZ   "
print(animal.upper())  # pasa todas las letras a mayusculas
print(animal.lower())  # pasa todas las letras a minusculas
print(animal.capitalize())  # pasa la primera letra a mayus, las demas en minus
print(animal.strip().capitalize())
# ejecuta la limpieza del strip y luego ejecuta el cmd de capitalize
print(animal.title())
# pasa la primera letra de cada palabra a mayus, las demas en minus
print(animal.strip())
# Elimina todos los espacios en blanco que contiene el string antes y despues del text
# existe el metodo lstrip que quita los espacios solo de la izq y rstrip que lo hace con los de la der
print(animal.find("ch"))
# Devuelve el indice del caracter en el string, si no se encuentra devolvera un -1
print(animal.replace("ch", "j"))
# reemplaza el primer caracter entregado por el segundo
print("nch" in animal)
# realiza una confirmacion si existe string indicado dentro de la variable, es true o false
print("nch" not in animal)
# es lo mismo que lo anterior pero negado, o sea busca si no se encuentra
