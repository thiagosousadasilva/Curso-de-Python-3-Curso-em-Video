''' 
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício.
Indo de 10 até 0, com uma pausa de 1 segundo entre eles.
'''
print("=========== desafio 046============")
from time import sleep

for t in range(10, 0, -1):
    print(t)
    sleep(1)
print('Boom!')