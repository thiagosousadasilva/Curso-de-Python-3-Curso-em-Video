# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.
print("=========== desafio 013 ============")
s = float(input('Informe o valor do salário do funcionário: '))
s = s + (s*0.15)
print('O novo valor do salário é de R$ {:.2f} já com 15% de aumento.'.format(s))