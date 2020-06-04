''' 
Exercício Python #094 - Unindo dicionários e listas:
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando 
os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
'''
print("== Exercício Python #094 - Unindo dicionários e listas: ==")
pessoas = []
while True:
    nome = input('Nome: ')
    sexo = input('Sexo [M/F]: ').upper()
    idade = int(input('Idade: '))
    pessoas.append({'nome': nome, 'sexo': sexo, 'idade': idade})
    esc = input('Continuar [S/N]: ')
    if esc in 'nN':
        break
print('-'*50)
print(f"A) Foram cadastradas {len(pessoas)} pessoas.")
total_idade = 0
for x in pessoas:
    total_idade += x['idade']
media_idade = total_idade/len(pessoas)
print(f"B) A média de idade: {media_idade:.0f} anos.")
print("C) Mulheres cadastradas: ")
for x in pessoas:
    if x['sexo'] == 'F':
        print('   -', x['nome'].title())
print("D) Pessoas com idade acima da média: ")
for x in pessoas:
    if x['idade'] >= media_idade:
        print('   -', x["nome"].title())
print('-'*50)        