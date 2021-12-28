# 8 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.

valor_hora = float(input("Informe seu ganho($) por hora: "))
h_trabalhadas = float(input("Informe a quantidade de horas trabalhadas no mês: "))

salario = valor_hora * h_trabalhadas

print("Seu salário no mês foi de : ", salario)
