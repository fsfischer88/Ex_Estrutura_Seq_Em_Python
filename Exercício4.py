# 4 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.

notas = []
soma_das_notas = 0


x = 1
n = 4

while x < 5:
    nota = float(input("Insira uma nota: "))
    x += 1
    notas.append(nota)
    print(notas)
    soma_das_notas += nota

media = soma_das_notas / n

print(media)
