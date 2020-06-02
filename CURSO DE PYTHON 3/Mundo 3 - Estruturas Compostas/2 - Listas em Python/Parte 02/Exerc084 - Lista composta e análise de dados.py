''' 
Exercício Python #084 - Lista composta e análise de dados:
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''
print("== Exercício Python #084 - Lista composta e análise de dados ==")
pessoas = []
pesado = leve = 0

while True:
    nome = input('Nome: ')
    peso = int(input('Peso: '))

    if len(pessoas) == 0:
        leve = peso
        pesado = peso
    else:
        if peso > pesado:
            pesado = peso    
        if peso < leve:
            leve = peso

    pessoas.append([nome, peso])            

    escolha = input('Deseja sair? [S/N] ')
    if escolha in 'sS':
        break

print('-'*50)
print(f'Foram cadastradas {len(pessoas)} pessoas!')

print(f'O maior peso foi {pesado}KG, das pessoas: ', end='')
for x, pessoa in enumerate(pessoas):
    if pessoa[1] == pesado:
        print(pessoa[0].capitalize(), end=' ')

print(f'\nO menor peso foi {leve}KG, das pessoas: ', end='')    
for x, pessoa in enumerate(pessoas):
    if pessoa[1] == leve:
        print(pessoa[0].capitalize(), end=' ')
print('\n')        
print('-'*50) 
