''' 
Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se
encontram no intervalo de 1 até 500.
'''
print("=========== desafio 048============")
soma = 0
lista = ''
for x in range(1, 500):
    if x % 2 != 0:
        if x % 3 == 0:
            soma += x
            lista += ', '+str(x)
print('Total da soma dos ímpares múltiplos de 3: {}'.format(soma))
print('Quantidade de itens somados: {}'.format(len(lista)))
print('Itens da soma:{}.'.format(lista))
    