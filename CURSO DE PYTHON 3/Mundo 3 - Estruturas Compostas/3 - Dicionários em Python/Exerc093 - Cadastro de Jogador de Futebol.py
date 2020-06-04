''' 
Exercício Python #093 - Cadastro de Jogador de Futebol:
Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. 
Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, incluindo o total 
de gols feitos durante o campeonato.
'''
print("== Exercício Python #093 - Cadastro de Jogador de Futebol: ==")
print('-'*50)
print(f'{"Cadastro de Jogador de Futebol":^50}')
print('-'*50)
nome = input('Nome do jogador: ')
partidas = int(input('Quantas partidas jogou? ')) 
lista_part = []
total_gols = 0
for x in range(1, partidas+1):
    gol = int(input(f'Gols na {x}ª partida: '))
    lista_part.append(gol)
    total_gols += gol
jogador = {'Nome': nome, 'Gols': lista_part, 'Total': total_gols}
print('-'*50)
print(f'{"Aproveitamento:":^50}')
print('-'*50)
print(f"- {jogador['Nome'].upper()} jogou {partidas} partidas.")
print(f"- Teve um total de {jogador['Total']} gol(s), sendo:")
for key, gol in enumerate(jogador['Gols']):
    print(f"   {key+1}ª partida: {gol} gol(s)")
print(f"Média de {jogador['Total']/partidas:.2f} gols por partida:  ")
print('-'*50)

