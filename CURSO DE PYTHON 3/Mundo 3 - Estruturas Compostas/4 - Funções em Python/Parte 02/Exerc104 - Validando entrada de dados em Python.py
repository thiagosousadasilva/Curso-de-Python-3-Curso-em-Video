''' 
Exercício Python #104 - Validando entrada de dados em Python:
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma
semelhante à função input() do Python, só que fazendo a validação para 
aceitar apenas um valor numérico. 
Ex: n = leiaInt('Digite um n: ')
'''
print("== Exercício Python #104 - Validando entrada de dados em Python ==")
def leia_int(texto):
    while True:
        num = input(texto)
        if num.isnumeric():
            return int(num)
        else:
            print('\033[1;31mDigite um número inteiro válido.\033[m')

# Programa principal
n = leia_int('Digite um número: ')
print(f'Você digitou o número {n}')