''' 
Exercício Python #088 - Palpites para a Mega Sena:
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 
6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
'''
print("== Exercício Python #088 - Palpites para a Mega Sena: ==")
from random import randint
num_jogos = int(input('Gerar quantos jogos? '))
num_jogos += 1
lista_jogos = []

for x in range(1, num_jogos):
    lista_temp = []    
    while len(lista_temp) < 6:
        num = randint(1, 60)
        if num not in lista_temp:
            lista_temp.append(num)
    lista_temp.sort()
    lista_jogos.append(lista_temp[:])
    lista_temp.clear()
for indice, jogos in enumerate(lista_jogos):
    print(f'Jogo {indice+1:>3} - {jogos}')
