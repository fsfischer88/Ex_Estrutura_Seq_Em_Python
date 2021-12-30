# 10 Faça um Programa que peça a temperatura em graus Celsius, 
# transforme e mostre em graus Fahrenheit.




temp_C = float(input("Digite a temperatura em Celsius: "))

if temp_C != 0:
    temp_F = ((1.8*temp_C)+32)
    print(temp_F)
else:
    print("A temperatura é 0 graus")