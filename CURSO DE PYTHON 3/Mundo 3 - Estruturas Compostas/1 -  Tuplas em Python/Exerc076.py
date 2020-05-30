''' 
Exercício Python #076 - Lista de Preços com Tupla
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos 
preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''
print("== Exercício Python #076 - Lista de Preços com Tupla ==")

lstprecos = ('Resma Papel A4', 16.90, 
             'Caneta Azul', 1.80, 
             'Régua 20cm', 3.25, 
             'Caderno 50fls', 2, 
             'Borracha Branca', 0.5,
             'Notebook Acer', 2560.7)
print('-'*40)
print(f'{"Lista de preços:":^36}')
print('-'*40)
for num_item in range(0, len(lstprecos)):
    if num_item % 2 == 0:
        print(f'\033[34m{lstprecos[num_item]:.<20} R$ {lstprecos[num_item + 1]:>7.2f}\033[m')
print('-'*40)
input('')