# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente 
# desse ângulo.
from math import sin, cos, tan, radians
print("=========== desafio 018 ============")
ang = radians(float(input('Informe o valor do ângulo: ')))
seno = sin(ang)
cosseno = cos(ang)
tangente = tan(ang)
print('Estes são respectivamente os valores de seno: {:.2f}, cosseno: {:.2f} e tangente {:.2f} do ângulo informado.'.format(seno, cosseno, tangente))