''' 
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem
pares. Se o valor digitado for ímpar, desconsidere-o.
'''
print("=========== desafio 050============")
soma = 0
lista = []
for x in range(1, 7):
    txt = str(x) + ' - Digite um número inteiro: '
    n = int(input(txt))
    if n % 2 == 0:
        soma += n
        lista.append(n)
print('Números pares: ', lista)
print('Total: ', soma)
