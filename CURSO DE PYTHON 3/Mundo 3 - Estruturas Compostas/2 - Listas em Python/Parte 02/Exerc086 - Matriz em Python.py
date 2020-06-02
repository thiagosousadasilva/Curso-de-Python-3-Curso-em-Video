''' 
Exercício Python #086 - Matriz em Python:
Crie um programa que declare uma matriz de dimensão 3x3 e preencha com 
valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
'''
print("== Exercício Python #086 - Matriz em Python: ==")
matriz = [[],[],[]]
for x in range(0,3):
    valor = int(input(f'Digite um valor para [0, {x}]: '))
    matriz[0].append(valor)
for x in range(0,3):
    valor = int(input(f'Digite um valor para [1, {x}]: '))
    matriz[1].append(valor)
for x in range(0,3):
    valor = int(input(f'Digite um valor para [2, {x}]: '))
    matriz[2].append(valor)    
print('-'*45)    
for itens in matriz:
    for item in itens:
        print(f'[{item:^5}]', end='')
    print('')