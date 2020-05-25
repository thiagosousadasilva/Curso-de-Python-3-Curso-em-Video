''' 
Crie um programa que faça o computador jogar jokenpô com você.
pedra - papel e tesoura
'''
from time import sleep
from random import choice
itens = ['PEDRA', 'PAPEL', 'TESOURA']
def valida(jog, comp):
    if comp == 0:
        if jog == 0:
            return 'Empate!'
        elif jog == 1:
            return 'O jogador venceu!'
        elif jog == 2:
            return 'O computador venceu!'       
    elif comp == 1:
        if jog == 0:
            return 'O computador venceu!'
        elif jog == 1:
            return 'Empate!'
        elif jog == 2:
            return 'O jogador venceu!'           
    elif comp == 2:
        if jog == 0:
            return 'O jogador venceu!'
        elif jog == 1:
            return 'O computador venceu!'
        elif jog == 2:
            return 'Empate!'

print("=========== desafio 045============")
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
''')
jogador = int(input('Qual é a sua jogada? '))
computador = choice([0, 1, 2])
resultado = valida(jogador, computador)
if jogador in range(0,3): 
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO!!!')
    sleep(0.5)
    print('-='*15)
    print('O computador jogou {}'.format(itens[computador]))
    print('O jogador jogou {}'.format(itens[jogador]))
    print('-'*10)
    print(resultado)
    print('-='*15)
else:
    print('Opção inválida!')
