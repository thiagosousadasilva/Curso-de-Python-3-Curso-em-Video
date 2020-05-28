''' 
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar 
quando o usuário digitar o valor 999, que é a condiçao de parada. No final, mostre quantos
números foram digitados e qual foi a soma entre eles. (desconsiderando o flag)
'''
print("==== Exercício Python #066 - Vários números com flag ====")
contador, soma = 0, 0

while True:
    n = int(input('Digite um inteiro (999 - p/ sair): '))
    if n == 999:
        break
    contador += 1
    soma += n
print(f'A soma dos {contador} números digitados é {soma}')