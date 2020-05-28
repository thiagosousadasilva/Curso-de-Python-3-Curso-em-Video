''' 
Crie um programa que simule o funcionamento de um caixa eletrônico. 
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o 
programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''
print("== Exercício Python #071 - Simulador de Caixa Eletrônico ==")
fmt = 0 #valor para formatar tamanho nº das cedulas
ced50, ced20, ced10, ced1 = 0, 0, 0, 0
print('='*35)
print('Banco CEV'.center(35))
print('-'*35)
valor_saque = int(input('Digite o valor do saque: '))
print('-'*35)

while valor_saque > 0:
    if valor_saque >= 50:
        ced50 += valor_saque // 50
        valor_saque = valor_saque % 50
        fmt = len(str(ced50))
        print(str(ced50).rjust(fmt), '- cédulas de R$ 50,00')
    if valor_saque >= 20:
        ced20 += valor_saque // 20
        valor_saque = valor_saque % 20
        print(str(ced20).rjust(fmt), '- cédulas de R$ 20,00')
    if valor_saque >= 10:
        ced10 += valor_saque // 10
        valor_saque = valor_saque % 10
        print(str(ced10).rjust(fmt), '- cédulas de R$ 10,00')
    if valor_saque >=1 and valor_saque < 10:
        ced1 += valor_saque
        valor_saque = 0
        print(str(ced1).rjust(fmt), '- cédulas de R$  1,00')
print('-'*35) 
print('Tenha um bom dia.'.center(35))
print('='*35) 