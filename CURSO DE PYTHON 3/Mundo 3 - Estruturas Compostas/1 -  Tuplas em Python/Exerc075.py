''' 
Exercício Python 075: Desenvolva um programa que leia quatro valores pelo 
teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
'''
print('''== Exercício Python #075 - Análise de dados em uma Tupla ==
''')
pares = ''
tupla = (int(input('Digite o 1º número: ')), int(input('Digite o 2º número: ')), int(input('Digite o 3º número: ')), int(input('Digite o 4º número: ')))

for num in tupla:
    if num % 2 == 0:
        pares += str(num)+' '

print(f'\nA) {tupla.count(9)} ocorrência(s) do número 9.')
if 3 in tupla:
    print(f'B) Na posição {tupla.index(3)} está a primeira ocorrência do número 3.')
else:
    print('B) Não há ocorrências do número 3.')
print(f'C) Número(s) par(es): {pares}')