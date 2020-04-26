# Faça um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
print("=========== desafio 012 ============")
p = float(input('Informe o preço do produto: '))
d = 5/100
np = p - (p*d)
print('O preço informado foi R$ {:.2f} e o seu novo valor é R$ {:.2f} com {} de desconto.'.format(p, np, '5%'))