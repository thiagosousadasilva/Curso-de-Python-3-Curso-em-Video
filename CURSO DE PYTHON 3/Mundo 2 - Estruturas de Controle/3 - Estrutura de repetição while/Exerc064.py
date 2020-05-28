''' 
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando
o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram
digitados e qual foi a soma entre eles (desconsiderando o flag.)
'''
print("==== #064 - Tratando vários valores v1.0 ====")
n, contador, soma = 0, 1, 0
n = int(input('Informe um número (999 - To Stop!):'))

while n != 999:
    contador += 1
    soma += n
    n = int(input('Informe outro número (999 - To Stop!):'))
        
print('\033[1;34mForam digitados {} números. E a soma é {}\033[m'.format(contador-1, soma))
print('Saindo...')