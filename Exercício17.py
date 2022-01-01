# 17 Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área 
# a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados 
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, 
# que custam R$ 25,00.

# o	Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# o	comprar apenas latas de 18 litros;
# o	comprar apenas galões de 3,6 litros;
# o	misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e 
# sempre arredonde os valores para cima, isto é, considere latas cheias.


import math # código que reune várias funções matemáticas


medida = float(input("Informe a área a ser pintada: "))
litros = ((medida*1)/6)
latas = math.ceil(litros / 3.6) # ceil = para pegar o teto da divisão 
print("Quantidade de latas é:",latas)
galoes = math.ceil(litros / 18) 
print("Quantidade de galoes é:",galoes)

preco_latas = latas*25
preco_galoes = galoes*80
combinacao = (litros // 18)*80 + (math.ceil(((litros % 18) / 3.6))*25) 
# Primeiro dividimos os litros por 18 e arredondamos para baixo = //. Depois multiplicamos por 80;
# Segundo pegamos o resto da divisão = % dos litros por 18 e então,
# dividimos por 3.6;
# Terceiro utilizamos o math.ceil para pegar o teto da divisão
# Quarto multiplicamos pelo custo da lata 3.6 = 25

print("O preço só com latas é: R$",preco_latas)
print("O preço só com galões é: R$",preco_galoes)
print("O preço com galões e latas é: R$",combinacao)


# area = float(input("Informe a área a ser pintada: "))
# cobertura_tinta = ((area*1)/6)
# custo_lata18 = 80
# litros_lata18 = 18
# custo_lata36 = 25
# litros_lata36 = 3.6

# qtd_latas = int(cobertura_tinta/litros_lata18)
# custo_total = (qtd_latas*custo_lata18)

# print("Cobertura da Tinta: ",int(cobertura_tinta),"litros/m²")
# print("Quantidade de latas: ", qtd_latas)
# print("Custo total: R$",custo_total)

# if cobertura_tinta <= 10.8:
#     latas = (cobertura_tinta/litros_lata36)
#     custo_total = latas*custo_lata36
#     print("Você precisa coprar",int(latas)," de 3,6 litros")
#     print("Custo total: R$",custo_total)
# elif cobertura_tinta > 10.8 and cobertura_tinta <= 18:
#     latas = (cobertura_tinta/litros_lata18)
#     custo_total = latas*custo_lata18
# else:
#     cobertura_tinta - 18
    