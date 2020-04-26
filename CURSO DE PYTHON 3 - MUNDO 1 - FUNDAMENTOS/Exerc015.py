# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por KM rodado.
print("=========== desafio 015 ============")
km = float(input('Informe quantos kilometros foram percorridos: '))
dias = float(input('Informe a quantidade de dias alugados: '))
preço = (dias * 60) + (km * 0.15)
print('O valor a pagar é de R$ {:.2f}.'.format(preço))