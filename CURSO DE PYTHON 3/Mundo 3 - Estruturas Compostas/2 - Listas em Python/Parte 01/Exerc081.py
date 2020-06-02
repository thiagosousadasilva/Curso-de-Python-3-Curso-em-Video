''' 
Exercício Python #081 - Extraindo dados de uma Lista:
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''
print("== Exercício Python #081 - Extraindo dados de uma Lista ==")
lista = []
valor = int(input('Digite um valor: '))
lista.append(valor)
while True:
    valor = int(input('Digite outro valor: '))
    lista.append(valor)
    escolha = input('Sair [y/n]: ')
    if escolha in 'Yy':
        break
lista.sort(reverse=True)
print('-'*40)
print(f'A) Número(s) digitado(s): {len(lista)}')
print(f'B) Lista: ', end='')
for item in lista:
    print(item, end=' ')
if 5 in lista:
    print(f'\nC) O valor 5 foi encontrado na lista.')
else:
    print(f'\nC) O valor 5 NÃO foi encontrado na lista.')
print('-'*40)
