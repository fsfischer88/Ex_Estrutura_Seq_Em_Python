# 16 Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área 
# a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados 
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

area = float(input("Informe a área a ser pintada: "))
cobertura_tinta = ((area*1)/3)
custo_lata = 80
litros_lata = 18

qtd_latas = int(cobertura_tinta/litros_lata)
custo_total = (qtd_latas*custo_lata)
print("Cobertura da Tinta: ",int(cobertura_tinta),"litros/m²")
print("Quantidade de latas: ", qtd_latas)
print("Custo total: R$",custo_total)


