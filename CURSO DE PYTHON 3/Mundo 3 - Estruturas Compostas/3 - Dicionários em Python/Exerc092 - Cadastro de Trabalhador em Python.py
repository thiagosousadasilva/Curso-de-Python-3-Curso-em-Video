''' 
Exercício Python #092 - Cadastro de Trabalhador em Python:
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e 
cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de
ZERO, o dicionário receberá também o ano de contratação e o salário. 
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''
print("== Exercício Python #092 - Cadastro de Trabalhador em Python: ==")
from datetime import date
trabalhador = {}
nome = input('Nome: ')
ano_nasc = int(input('Ano de nascimento: '))
ctps = input('Carteira de Trabalho (0 não tem): ')
if ctps != '0':
    ano_contrat = int(input('Ano da contratação: '))
    salario = float(input('Salário: '))
    trabalhador = {'nome': nome, 'idade': date.today().year-ano_nasc, 
    'ctps': ctps, 'contratação': ano_contrat, 
    'salário': salario, 
    'idade_aposenta': ((ano_contrat+35)-date.today().year)+(date.today().year-ano_nasc)}
else:
    trabalhador = {'nome': nome, 'idade': date.today().year-ano_nasc} 
print('|'+'-'*35+'|')
print(f'|{"Dados do trabalhador:":^35}|')
print('|'+'-'*35+'|')
for chave, valor in trabalhador.items():
    texto = f'{chave.title()}: {str(valor).title()}'
    print(f'| {texto:<34}|')
print('|'+'_'*35+'|')