''' 
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não
atingiram a maioridade e quantas já são maiores (considerar 21 anos para maioridade).
'''
print("=========== desafio 054============")
import datetime
maiores = 0
menores = 0
for x in range(1, 8):
    print(x, end= ' - ')
    ano = (int(input('Informe o ano de nascimento: ')))
    print(datetime.date.today().year - ano)
    if (datetime.date.today().year - ano) > 20:
        maiores += 1
    else:
        menores += 1
print('{} maiores de idade e {} menores de idade'.format(maiores, menores))      