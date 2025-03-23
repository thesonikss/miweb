# Funcion para eliminar espacios en blanco de un string
def no_space(texto):
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto


# Funcion para dar vuelta un string
def reverse(texto):
    texto_al_reves = ""
    for char in texto:
        texto_al_reves = char + texto_al_reves

    return texto_al_reves


# Compara ambas funciones y las convierte en minusculas
def es_palindromo(texto):
    texto = no_space(texto)
    texto_al_reves = reverse(texto)
    return texto.lower() == texto_al_reves.lower()


print(es_palindromo("hehehe"))
