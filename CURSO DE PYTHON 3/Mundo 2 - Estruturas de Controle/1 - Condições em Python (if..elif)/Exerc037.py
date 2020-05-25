''' 
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base da conversão:
- 1 para binário.
- 2 para octal.
- 3 para hexadecimal.
'''
print("=========== desafio 037============")
n = int(input('Informe o número inteiro para conversão: '))
base = int(input('''Informe qual a base de conversão: 
    -> 1 para binário.
    -> 2 para octal.
    -> 3 para hexadecimal. 
'''))
print(21*'=-'+'=')
if base == 1:
    print('Binário: {}'.format(bin(n)))
elif base == 2:
    print('Octal: {}'.format(oct(n)))
elif base == 3:
    print('Hexadecimal: {}'.format(hex(n)))
print(21*'=-'+'=')