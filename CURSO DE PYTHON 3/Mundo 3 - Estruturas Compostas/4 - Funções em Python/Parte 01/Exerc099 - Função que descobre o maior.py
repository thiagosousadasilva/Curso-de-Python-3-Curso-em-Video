''' 
Exercício Python #099 - Função que descobre o maior:
Faça um programa que tenha uma função chamada maior(), 
que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''
print("== Exercício Python #099 - Função que descobre o maior ==")
from time import sleep
def maior(*num):
    cont = 0
    maior = 0
    print('-'*50)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor}', end=' ')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')

maior(3,4,2,8,1,10)
maior(4,7,0)
maior(1,2)
maior(6)
maior()


