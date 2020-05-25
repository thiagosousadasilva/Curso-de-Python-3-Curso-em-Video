''' 
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
import datetime
print("=========== desafio 039============")
ano = int(input('Qual o ano de nascimento: '))
print(18*'=-'+'=')
idade = datetime.date.today().year - ano
if idade < 18:
    print('Você deverá se alistar em {} ano(s)'.format(18-idade))
elif idade == 18:
    print('Está na hora de se alistar!')
else:
    print('Já passou do tempo do alistamento.')