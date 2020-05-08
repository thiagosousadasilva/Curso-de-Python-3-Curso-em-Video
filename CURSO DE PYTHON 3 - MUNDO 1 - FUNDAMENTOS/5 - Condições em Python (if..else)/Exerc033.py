''' 
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''
print("=========== desafio 033============")
lista = []
lista.append(float(input('informe o primeiro número: ')))
lista.append(float(input('Informe o segundo número: ')))
lista.append(float(input('Informe o terceiro número: ')))
lista.sort()
print('{} < {} < {}'.format(lista[0], lista[1], lista[2]))

