''' 
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7,00 por cada km acima do limite.
'''
print("=========== desafio 029 ============")
from math  import ceil
vel = ceil(float(input('Digite a velocidade do carro: ')))
if vel > 80:
    print('Você foi multado! Para a velocidade {}km/h o valor da multa é de R$ {:.2f}'.format(vel, (vel - 80)* 7))
else:
    print('Tudo ok!')