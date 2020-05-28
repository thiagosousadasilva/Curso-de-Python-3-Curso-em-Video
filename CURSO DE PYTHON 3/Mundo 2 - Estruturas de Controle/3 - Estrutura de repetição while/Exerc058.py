''' 
Melhore o jogo do DESAFIO 028 onde o computador vai 'pensar' em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
foram necessários para vencer.
'''
print("=========== desafio 058============")
from random import randint
num_comp = randint(0,11)
tentativas = 1

print('\033[0;35mO computador escolheu um número entre 0 e 10.')
num_user = int(input('Tente descobrir qual foi o número:\033[m '))

while num_comp != num_user:
    print('\033[1;31mVocê errou!\033[m')
    num_user = int(input('Tente novamente: '))
    tentativas += 1

print('\033[1;32mVocê acertou! O número era o:', num_comp)
print('Foram {} tentativas até acertar.\033[m'.format(tentativas))