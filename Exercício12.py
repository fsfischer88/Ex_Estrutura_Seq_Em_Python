# 12 Tendo como dados de entrada a altura de uma pessoa,
#  construa um algoritmo que calcule seu peso ideal, 
#  usando a seguinte fórmula: (72.7*altura) - 58

peso_atual = float(input("Informe seu peso atual: "))
altura = float(input("Informe sua altura: "))


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

