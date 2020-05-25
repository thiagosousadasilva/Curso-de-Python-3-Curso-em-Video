''' 
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e 
mostre sua categoria, de acordo com a idade:
- até 9 anos: mirim
- até 14 anos: infantil
- até 19 anos: junior
- até 20 anos: sênior
- acima: master
'''
from datetime import date
print("=========== desafio 041============")
ano = int(input('Informe o ano de nascimento: '))
idade = date.today().year - ano
if  idade <= 9:
    print('Idade: {} - Categoria Mirim'.format(idade))
elif idade > 9 and idade <= 14:
    print('Idade: {} - Categoria Infantil.'.format(idade))
elif idade > 14 and idade <= 19:
    print('Idade: {} - Categoria Junior.'.format(idade))
elif idade == 20:
    print('Idade: {} - Categoria Sênior'.format(idade))
elif idade > 20:
    print('Idade: {} - Categoria Master'.format(idade))
