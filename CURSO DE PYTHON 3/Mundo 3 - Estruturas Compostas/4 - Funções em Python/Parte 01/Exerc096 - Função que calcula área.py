''' 
Exercício Python #096 - Função que calcula área:
Faça um programa que tenha uma função chamada área(), 
que receba as dimensões de um terreno retangular 
(largura e comprimento) e mostre a área do terreno.
'''
print("== Exercício Python #096 - Função que calcula área ==")
def area(x,y):
    return x * y

largura = float(input('Largura do retângulo: '))
comprimento = float(input('Comprimento do retângulo: '))
print(f"A área do terreno é: {area(largura, comprimento)}")