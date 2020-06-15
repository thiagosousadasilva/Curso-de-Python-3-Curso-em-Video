''' 
Exercício Python #103 - Ficha do Jogador:
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros
opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser 
capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado 
corretamente.
'''
print("== Exercício Python #103 - Ficha do Jogador ==")
def ficha(nome='<desconhecido>', gols=0):
    if gols.isnumeric():
        return f'O jogador {nome} fez {gols} gol(s) no compeonato.'
    else:
        gols = 0
        return f'O jogador {nome} fez {gols} gol(s) no compeonato.' 

nome = input('Nome do jogador: ')
gols = input('Número de gols: ')
print(ficha(nome, gols))