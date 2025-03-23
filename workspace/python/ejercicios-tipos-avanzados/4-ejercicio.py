notas = [("Pedro", 3.4), ("Juan", 8.5), ("Daniel", 6.8), ("Camila", 6.8)]
mejores_notas = []
nota_acumulada = 0.0

for alumnos, nota in notas:
    if nota >= nota_acumulada:
        nota_acumulada = nota


for acumulado in notas:
    if acumulado[1] >= nota_acumulada:
        mejores_notas.append(acumulado)
print(mejores_notas)
