# 18 Faça um programa que peça o tamanho de um arquivo para download (em MB) e 
# a velocidade de um link de Internet (em Mbps), 
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)


tam_arq = int(input("Informe o tamanho do arquivo em mb: "))
velocidade = int(input("Informe a velocidade em Mbps: "))

dowload = tam_arq/ velocidade
conversao = dowload/60

print("Tempo estimado para Download: ",conversao,"minutos")
