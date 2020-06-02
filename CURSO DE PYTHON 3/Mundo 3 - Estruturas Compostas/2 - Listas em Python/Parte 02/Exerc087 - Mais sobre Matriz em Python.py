''' 
Exercício Python #087 - Mais sobre Matriz em Python:
Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''
print("== Exercício Python #087 - Mais sobre Matriz em Python: ==")
matriz = [[],[],[]]
pares = ter_coluna = 0
for x in range(0, 3):
    for y in range(0,3):
        valor = int(input(f'Digite um valor para [{x}, {y}]: '))
        matriz[x].append(valor)
        if valor % 2 == 0:
            pares += valor
        if y == 2:
            ter_coluna += valor
print('-'*45)
for itens in matriz:
    for item in itens:
        print(f'[{item:^5}]',end='')
    print()
print('-'*45)
print('A) Soma dos nº pares:', pares)
print('B) Soma dos nº da 3ª coluna:', ter_coluna)
matriz[1].sort()
print('C) Maior valor da 2ª linha:', matriz[1][-1])
print('-'*45)