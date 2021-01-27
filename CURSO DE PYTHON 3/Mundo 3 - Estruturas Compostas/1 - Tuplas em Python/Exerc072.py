''' 
Exercício Python 072: Crie um programa que tenha uma tupla totalmente preenchida 
com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número
pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''
print("== Exercício Python #072 - Número por Extenso ==")

num_extenso = ('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 
'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
escolha = input('Digite um número entre 0 e 20: ')
print(f'\033[1;34m{num_extenso[int(escolha)].capitalize()}\033[m')
