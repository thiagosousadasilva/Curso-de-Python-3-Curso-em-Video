''' 
Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5x4x3x2x1 = 120
'''
print("=========== desafio 060============")
from math import factorial

n = int(input('Digite o número: '))
fat = factorial(n)
frase = []
contador = n

while contador > 0:
    frase.append(str(contador))
    contador -= 1
print('\033[35m', end='')
print('*'*25)
print('\033[1;32m{}! = {} = {} \033[m'.format(n, 'x'.join(frase), fat))
print('\033[35m', end='')
print('*'*25)