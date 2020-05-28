''' 
Escreva um programa que leia um número 'n' inteiro qualquer e mostre na tela os 'n' 
primeiros elementos de uma Sequência de Fibonacci.
Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
'''
print('=========== desafio 063============')

nTermos = int(input('Quantos elementos da Sequência de Fibonacci você quer? '))
lstTermos = []
Fn1 = 0
Fn2 = 1
x = 0

while x < nTermos:
    lstTermos.append(str(Fn1))
    Fn = Fn1 + Fn2
    Fn1 = Fn2
    Fn2 = Fn
    x += 1

print(' > '.join(lstTermos))