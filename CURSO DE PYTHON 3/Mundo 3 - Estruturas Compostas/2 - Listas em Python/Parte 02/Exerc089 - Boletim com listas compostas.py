''' 
Exercício Python #089 - Boletim com listas compostas:
Crie um programa que leia nome e duas notas de vários alunos e guarde 
tudo em uma lista composta. No final, mostre um boletim contendo a média
de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
'''
print("== Exercício Python #089 - Boletim com listas compostas: ==")
lista_alunos = []
while True:
    nome = input('Nome: ')
    n1 = float(input('1ª nota: '))
    n2 = float(input('2ª nota: '))
    lista_alunos.append([nome, n1, n2])    
    escolha = input("Continuar [S/N]: ")
    print('-'*23)    
    if escolha in 'nN':
        break
print('-'*35)
print(f'Cód. {"Nome":<20} Média')
print('-'*35)
for x, alunos in enumerate(lista_alunos):
    print(f'{x:^4} {alunos[0].title():<20} {(alunos[1]+alunos[2])/2:>5.2f}')
print('-'*35)
while True:
    escolha = int(input('Digite o cód. do aluno para ver as notas (999 p/ sair): '))
    print('-'*60)    
    if escolha != 999:
        if escolha < len(lista_alunos):
            print(f"\033[1;34mAs notas de {lista_alunos[escolha][0].title()} são: {lista_alunos[escolha][1]} e {lista_alunos[escolha][2]}\033[m")
            print('-'*60)
        else:
            print('\033[1;31mCódigo inexistente! Tente outra vez.\033[m')
            print('-'*60)
    else:
        break
print('Fechando...')