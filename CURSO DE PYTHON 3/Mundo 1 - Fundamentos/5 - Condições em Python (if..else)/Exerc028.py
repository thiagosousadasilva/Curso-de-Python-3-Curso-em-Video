''' 
Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
print("=========== desafio 028 ============")
from random import randint
import colorama
colorama.init()
a = ''
print('O computador já escolheu um número entre 0 e 5.')
while a != 'sair':

    a = input('Digite um número entre 0 e 5 e veja se acertou: ')
    b = str(randint(0,5))
    if a == b:
        print('\033[0;33;44m Parabéns! Você acertou! \033[m')
    else:
        if a == 'sair': 
            print('Fechando...')
        else:
            print('\033[4;30;45m Você errou! O Número era: {} \033[m'.format(b))
    print(50*'-')