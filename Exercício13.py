# 13   Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
# utilizando as seguintes fórmulas:
#   Para homens: (72.7*h) - 58
#   Para mulheres: (62.1*h) - 44.7


peso_atual = float(input("Informe seu peso atual: "))
altura = float(input("Informe sua altura: "))
sexo = input("Informe seu sexo. M para masculino e F para feminino: ")

if sexo == "M":
    peso_ideal = ((72.7*altura) - 58)
    print(peso_ideal)
    if peso_atual >= peso_ideal:
        dif_peso = peso_atual - peso_ideal
        print("Você está acima do peso. Você está ",dif_peso,"kg acima do peso ideal")
    elif peso_atual == peso_ideal:
        print("Você está no seu peso ideal. Parabéns!")
    else:
        dif_peso = peso_ideal - peso_atual
        print("Você está abaixo do seu peso ideal em ",dif_peso,"kg")
elif sexo == "F":
    peso_ideal = ((62.1*altura) - 44.7)
    print(peso_ideal)
    if peso_atual >= peso_ideal:
        dif_peso = peso_atual - peso_ideal
        print("Você está acima do peso. Você está ",dif_peso,"kg acima do peso ideal")
    elif peso_atual == peso_ideal:
        print("Você está no seu peso ideal. Parabéns!")
    else:
        dif_peso = peso_ideal - peso_atual
        print("Você está abaixo do seu peso ideal em ",dif_peso,"kg")
else:
    print("Você não digitou uma opção válida. Digite M ou F")