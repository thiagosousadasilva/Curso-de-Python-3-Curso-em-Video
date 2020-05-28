''' 
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média
entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário
se ele quer ou não continuar a digitar valores.
'''
print("=========== desafio 065============")
n, contador, total, maior, menor = 0, 0, 0, 0, 0

while n != 'N':
    n = input('Informe o número ("N" para sair): ').upper()
    if n != 'N':
        total += int(n)
        if contador == 0:
            menor = int(n)
            maior = int(n)
        else:
            if int(n) < menor:
                menor = int(n)
            elif int(n) > maior:
                maior = int(n)
    contador += 1
print('A média é {} | O menor é {} | O maior é {}'.format(total/(contador-1), menor, maior))