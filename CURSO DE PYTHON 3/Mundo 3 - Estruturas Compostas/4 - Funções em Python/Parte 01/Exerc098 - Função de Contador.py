''' 
Exercício Python #098 - Função de Contador:
Faça um programa que tenha uma função chamada contador(), 
que receba três parâmetros: início, fim e passo. 
Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
'''
print("== Exercício Python #098 - Função de Contador ==")
from time import sleep
def contador(inicio, fim, passo):
    print('-'*50)     
    for z in range(inicio, fim+1, passo):
        print(z, end=' ')
        sleep(0.5)
    print('\n'+'-'*50)  

print('-'*50)
print('A) Contagem de 1 até 10, de 1 em 1:')
contador(1, 10, 1) 

print('B) Contagem de 10 até 0, de 2 em 2:')
contador(10, 0, -2)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)