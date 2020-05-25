''' 
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo (divisivel apenas
por 1 e por ele mesmo).
'''
print("=========== desafio 052============")
n = int(input('Digite um número: '))
total = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[32m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print(c, end='')
print('\n\033[mO número {} foi divisível {} vezes.'.format(n, total))
if total == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO é primo!')
print('==='*10)