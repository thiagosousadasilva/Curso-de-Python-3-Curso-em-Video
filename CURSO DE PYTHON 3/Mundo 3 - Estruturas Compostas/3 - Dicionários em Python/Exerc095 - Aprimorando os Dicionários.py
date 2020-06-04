''' 
Exercício Python #095 - Aprimorando os Dicionários:                                                                                                             
Aprimore o desafio 93 para que ele funcione com vários jogadores, 
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
'''
print("== Exercício Python #095 - Aprimorando os Dicionários ==")
jogadores = []
while True:
    nome = input('Nome do jogador: ').title()
    partidas = int(input('Jogou quantas partidas? '))
    gols = []
    tot_gol = 0
    for x in range(1, partidas+1):
        gol_part = int(input(f"{x}ª partida: "))
        gols.append(gol_part)
        tot_gol += gol_part
    jogadores.append({'nome': nome, 'part': partidas, 'gols': gols, 'tot_gol': tot_gol})
    esc = input('Continuar [S/N]: ')
    if esc in 'nN':
        break
    print('-'*40)
print('-'*50)
print(f"{'Relatório de jogadores':^50}")
print('-'*50)
print(f"Total de {len(jogadores)} jogadores cadastrados.")
for key, valor in enumerate(jogadores):
    print(f"{key} - {valor['nome']}")
while True:
    print('-'*50)    
    cod = int(input('Código do jogador p/ detalhes ou 999 para sair: '))
    if cod == 999:
        break
    else:
        print('-'*50)            
        print(f"- {jogadores[cod]['nome']} jogou {jogadores[cod]['part']} partidas.")
        print(f"-- Marcou {jogadores[cod]['tot_gol']} gols. Sendo:")
        for x, gol in enumerate(jogadores[cod]['gols']):
            print(f"--- {gol} gol(s) na {x+1}ª partida.")
        print(f"- Média de {jogadores[cod]['tot_gol']/jogadores[cod]['part']:.2f} gols por partida.")
print('-'*50) 
print('Fechando...')