# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Exemplo: Digite um número: 6.127
#          O número 6.127 tem a parte inteira 6
# dica: olhar as classes do módulo math. 
print("=========== desafio 016 ============")
from math import trunc
n = float(input('Informe um número real: '))
i = trunc(n)
print('O número {} é a porção inteira do número real {}.'.format(i, n))
