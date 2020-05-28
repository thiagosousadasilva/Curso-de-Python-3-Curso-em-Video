''' 
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando 
o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 
'''
print("== Exercício Python #068 - Jogo do Par ou Ímpar ==")
print('-'* 30)
print('Vamos jogar PAR ou ÍMPAR!')
print('-'* 30)
from random import randint 
contador = 0
while True:
    computador = randint(0, 5)
    jogador = int(input('Diga um valor entre 0 e 5: '))
    escolha = input('Escolha Par ou Ímpar [P/I]: ').upper()
    soma = jogador + computador
    while escolha not in 'PI':
        escolha = input('Escolha Par ou Ímpar [P/I]: ').upper()
    if (soma % 2 == 0 and escolha == 'P') or (soma % 2 != 0 and escolha == 'I'):
        print(f'Você GANHOU! O computador escolheu {computador}')
        contador += 1
    else:
        print(f'Você PERDEU! O computador escolheu {computador}')
        break
print(f'Você venceu {contador} vez(es)!')



