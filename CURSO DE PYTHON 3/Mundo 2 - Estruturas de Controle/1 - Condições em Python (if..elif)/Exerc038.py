''' 
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior.
- O segundo valor é maior.
- Não existe valor maior, os dois são iguais.
'''
print("=========== desafio 038============")
n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
if n1 > n2:
    print('\033[1;34m O primeiro valor é maior.\033[m')
elif n1 < n2:
    print('\033[1;32m O segundo valor é maior.\033[m')
else:
    print('\033[1;31m Não existe valor maior, os dois são iguais.\033[m')