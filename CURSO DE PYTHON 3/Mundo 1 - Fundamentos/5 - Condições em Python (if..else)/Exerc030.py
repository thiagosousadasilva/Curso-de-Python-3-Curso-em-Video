''' 
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.
'''
print("=========== desafio 030 ============")
n = int(input('Digite um número para verificar se ele é PAR ou IMPAR: '))
if n%2 == 0:
    print('O número {} é PAR!'.format(n))
else:
    print('O número {} é IMPAR!'.format(n))