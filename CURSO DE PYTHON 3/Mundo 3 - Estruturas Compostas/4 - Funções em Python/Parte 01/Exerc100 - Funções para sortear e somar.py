''' 
Exercício Python #100 - Funções para sortear e somar:
Faça um programa que tenha uma lista chamada números e duas funções
chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números
e vai colocá-los dentro da lista e a segunda função vai mostrar a soma 
entre todos os valores pares sorteados pela função anterior.
'''
print("== Exercício Python #100 - Funções para sortear e somar ==")
from random import randint
numeros = []

def sorteia():
    while len(numeros) < 5:
        numeros.append(randint(0, 1000))

def somapar(lista):
    soma = 0
    pares = ''
    print('-'*50)  
    print(f"\033[32mNúmeros sorteados:", end=' ')
    for x in sorted(lista):
        print(x, end=' ')
        if x %2 == 0:
            soma += x
            pares += str(x)+' + '
    print('\033[m')
    print('-'*50)
    print(f"\033[1;34mSoma dos números pares: {pares[:-3]} = {soma}\033[m")
    print('-'*50)
sorteia()
somapar(numeros)