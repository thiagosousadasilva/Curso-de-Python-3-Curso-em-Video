''' 
Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e 
colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também
indique o menor e o maior valor que estão na tupla.
'''
print("== Exercício Python #074 - Maior e menor valores em Tupla ==")
from random import randint
numeros = [randint(0, 1000), randint(0, 1000), randint(0, 1000), randint(0, 1000), randint(0, 1000)]
print('Lista de números:')
for num in numeros:
    print(num, end=' ')
print('\nMenor:', max(numeros))
print('Maior:', min(numeros))