# Crie um programa que leia quanto uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere US$ = R$ 3,27.
print("=========== desafio 010 ============")
d = 3.27
n = float(input('Digite quanto tem na carteira: '))
print('Você pode comprar US$ {:.2f}'.format(n/d))