''' 
Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. 
'''
print("=== Exercício Python #070 - Estatísticas em produtos ==")
total_gasto = 0
mais_1000 = 0
mais_barato = ''
menor_preco = 0
escolha = 'n'
while escolha != 'S':
    produto = input('Nome do produto: ')
    preco = float(input('Preço: '))
    escolha = input('Deseja sair [S/N]: ').upper()
    total_gasto += preco
    if preco > 1000:
        mais_1000 += 1
    if menor_preco > preco or menor_preco == 0:
        menor_preco = preco
        mais_barato = produto.capitalize()

print(f'Total gasto na compra R$: {total_gasto:.2f}')
print(f'{mais_1000} produto(s) custa(m) mais que R$ 1000.')
print(f'O {mais_barato} é produto mais barato: R$ {menor_preco}')
