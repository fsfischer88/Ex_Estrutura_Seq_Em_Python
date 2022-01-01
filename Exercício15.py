# 15 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o 
# Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

# o	salário bruto.
# o	quanto pagou ao INSS.
# o	quanto pagou ao sindicato.
# o	o salário líquido.
# o	calcule os descontos e o salário líquido, conforme a tabela abaixo:
# o	+ Salário Bruto : R$
# o	- IR (11%) : R$
# o	- INSS (8%) : R$
# o	- Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

salario_hora = float(input("Informe seu ganho($) por hora: "))
horas_trab = float(input("Informe suas horas trabalhadas: "))

salario_bruto = (salario_hora*horas_trab)
print("Seu salário Bruto é: R$",salario_bruto)

imposto_renda = (salario_bruto*0.11)
print("IR: R$", imposto_renda)

inss = (salario_bruto*0.08)
print("INSS: R$", inss)

sindicato = (salario_bruto*0.05)
print("Sindicato: R$", sindicato)

descontos = (imposto_renda + inss + sindicato)
print("Total Descontos: R$", descontos)

salario_liquido = (salario_bruto - descontos)
print("Salarío Líquido: R$", salario_liquido)



