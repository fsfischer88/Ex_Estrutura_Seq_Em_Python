# 9	Faça um Programa que peça a temperatura em graus Fahrenheit, 
# transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).


temp_F = float(input("Digite a temperatura em Fahrenheit: "))

if temp_F != 0:
    temp_c = 5 * ((temp_F-32) / 9)
    print(temp_c)
else:
    print("A temperatura é 0 graus")