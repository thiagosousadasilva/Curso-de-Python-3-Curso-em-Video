''' 
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, 
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. 
'''
print("== Exercício Python #069 - Análise de dados do grupo ==")
maior18 = 0
homens = 0
mulher20 = 0
pessoas = 0

print('-'*30)
while True:
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper()
    escolha = input('Deseja continuar? [S/N]').upper()
    pessoas += 1    
    print(idade, sexo, escolha)
    print('-'*30)

    if idade >= 18:
        maior18 += 1
    if sexo == 'M':
        homens += 1    
    if sexo == 'F' and idade < 20:
        mulher20 += 1    
    if escolha == 'N':
        break
    
print('\033[1;34m', end='')
print('Total de pessoas cadastradas:', pessoas)
print(f'Maiores de 18 anos:', maior18)
print(f'Homens:', homens)
print(f'Mulheres com menos de 20 anos:', mulher20)
print('\033[m', end='')
print('-'*30)
print('Fechando...')