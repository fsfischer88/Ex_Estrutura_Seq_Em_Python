# 11  Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# 	o produto do dobro do primeiro com metade do segundo .
# 	a soma do triplo do primeiro com o terceiro.
# 	o terceiro elevado ao cubo.



numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
numero_real = float(input("Digite um número real: "))


produto = ((numero1*2) * (numero2/2))
print(produto)

soma = ((numero1*3) + (numero_real))
print(soma)

cubo = (numero_real**3)
print(cubo)