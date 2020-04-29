# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
# triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
# h² = Co² + Ca² - ou usar pronto no modúlo math
import math
print("=========== desafio 017 ============")
CatOp = float(input('Informe o comprimento do cateto oposto: '))
CatAd = float(input('informe o comprimento do cateto adjacente: '))
Hip = math.hypot(CatOp, CatAd)
print('A hipotenusa é {}'.format(Hip))