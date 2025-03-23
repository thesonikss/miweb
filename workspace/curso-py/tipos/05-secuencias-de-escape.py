curso1 = "Ultimate Python"
curso2 = "Ultimate Python"
# Esto no lo permite ya que el interprete de python va a pensar que primero cierras las comillas, y luego abres las siguientes
curso3 = "Ultimate 'Python'"  # esto es valido
curso4 = 'Ultimate "Python"'  # esto es valido
curso5 = "Ultimate \"Python\""
# con el backslash le indicamos que lo escrito a continuacion sera parte del string
# si quisieramos poner un backslash dentro de nuestro codigo deberiamos poner dos backslash seguidos \\
curso6 = "Ultimate \nPython"
# Genera un salto de linea
print(curso3)
