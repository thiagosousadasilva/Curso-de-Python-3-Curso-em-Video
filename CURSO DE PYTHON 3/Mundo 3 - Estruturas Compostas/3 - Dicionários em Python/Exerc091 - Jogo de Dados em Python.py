''' 
Exercício Python #091 - Jogo de Dados em Python:
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python. No final, coloque esse 
dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
'''
print("== Exercício Python #091 - Jogo de Dados em Python: ==")
from random import randint
from time import sleep
jogadores = {'Jogador A': randint(1, 6), 
'Jogador B': randint(1, 6), 
'Jogador C': randint(1, 6), 
'Jogador D': randint(1, 6)}
for chave, valor in jogadores.items():
    print(f'O {chave} tirou: {valor}')
    sleep(1)
print('-'*50)    
ranking = sorted(jogadores.items(), key = lambda x: x[1], reverse = True)
for n, item in enumerate(ranking):
    print(f'{n+1}º lugar: {item[0]} com {item[1]}')
    sleep(1)