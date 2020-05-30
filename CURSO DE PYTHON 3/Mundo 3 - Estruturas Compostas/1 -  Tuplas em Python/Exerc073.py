''' 
Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense.
'''
print("== Exercício Python #073 - Tuplas com Times de Futebol ==")
tabela = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico', 'São Paulo', 
'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Gama',
'Atlético', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
print('=' * 40)
print('Relatório Brasileirão 2019'.center(40))
print('=' * 40)
print('a) Os 5 primeiros times:\n')
# a) Os 5 primeiros times.
for time in tabela[:5]:
    print(f'{tabela.index(time)+1}º {time}')

# b) Os últimos 4 colocados.
print('-' * 40)
print('b) Os últimos 4 colocados.\n')
for time in tabela[-4:]:
    print(f'{tabela.index(time)+1}º {time}')

# c) Times em ordem alfabética.
print('-' * 40)
print('c) Times em ordem alfabética.\n')
lst_tbl = list(tabela)
lst_tbl.sort()
for time in lst_tbl:
    print(time)

# d) Em que posição está o time da Chapecoense.
print('-' * 40)
print('d) Em que posição está o time da Chapecoense.\n')
print(f"{tabela.index('Chapecoense') + 1}ª posição!")    
print('-' * 40)