# 14 João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário
#  de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca
# do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa 
# que João deverá pagar. 
# Imprima os dados do programa com as mensagens adequadas.


peso_peixes = float(input("Digite o peso dos peixes: "))
multa_total = []
multa = 4
excesso = []


if peso_peixes < 50:
    print("Peso dos peixes está ok!")
else:
    excesso = (peso_peixes - 50)
    print(excesso)
    multa_total = (excesso*multa)
    print(multa_total)
    print("O valor total da multa a ser pago foi de: R$",multa_total)