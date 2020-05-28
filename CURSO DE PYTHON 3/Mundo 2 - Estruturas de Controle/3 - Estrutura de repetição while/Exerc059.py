''' 
Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''
print("=========== desafio 059============")
opcao = ''
n1 = float(input('Informe o primeiro valor: '))
n2 = float(input('Informe o segundo valor: '))
while opcao != 5:
    print('''______________________________

Escolha sua opção: 
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
''')

    opcao = int(input(''))
    if opcao == 5:
        print('\033[36mFechando programa...\033[m')
    else:
        print('''______________________________
Resultado: ''')
        if opcao == 1:
            print('\033[32m{} + {} = {}\033[m'.format(n1, n2, n1 + n2))
        elif opcao == 2:
            print('\033[32m{} x {} = {}\033[m'.format(n1, n2, n1 * n2))
        elif opcao == 3:
            if n1 > n2:
                print('\033[32mO {} é maior que {}\033[m'.format(n1, n2))
            elif n1 < n2:
                print('\033[32mO {} é maior que {}\033[m'.format(n2, n1))
            else:
                print('\033[32mNão há maior, os números são iguais.\033[m')
        elif opcao == 4:
            n1 = float(input('Primeiro novo valor: '))
            n2 = float(input('Segundo novo valor: '))