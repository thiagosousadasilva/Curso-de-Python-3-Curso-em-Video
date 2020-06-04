''' 
 Exercício Python #090 - Dicionário em Python:
 Faça um programa que leia nome e média de um aluno,  guardando também 
 a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
'''
print("== Exercício Python #090 - Dicionário em Python ==")
dicionario = {}
dicionario['nome']= input('Nome: ')
dicionario['media'] = float(input('Média: '))
if dicionario['media'] >= 7:
    dicionario['situacao'] = 'Aprovado'
else:
    dicionario['situacao'] = 'Reprovado'
print(f"O aluno {dicionario['nome']} está {dicionario['situacao'].upper()} pois tem a média {dicionario['media']}.")
    