''' 
Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que
agora utilizando um laço for.
'''
print("=========== desafio 049============")
n = int(input('Escolha o número da tabuada: '))
print('''Operações:
[0] ADIÇÃO
[1] SUBTRAÇÃO
[2] MULTIPLICAÇÃO
[3] DIVISÃO
''')
op = int(input('Escolha a operação da tabuada: '))
if op == 0:
    for x in range(1 , 11):
        print('{} + {} = {}'.format( n, x, x + n))
elif op == 1:
    for x in range(1, 11):
        print('{} - {} = {}'.format(n, x, x - n))
elif op == 2:
    for x in range(1, 11):
        print('{} x {} = {}'.format(n, x, n * x))
elif op == 3:
    for x in range(1, 11):
        print('{} / {} = {:.1f}'.format( n, x, n / x))