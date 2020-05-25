''' 
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo(quando lida ao contrário tem o 
mesmo significado), desconsiderando os espaços entre as palavras(remover os espaços).
'''
print("=========== desafio 053============")
frase = input('Digite uma frase: ')
frs = ''
for letra in frase:
    if letra != ' ':
        frs += letra.lower()
if frs == frs[::-1]:
    print('\033[1;32mA frase informada é um PALÍNDROMO\033[m')
else:
    print('\033[1;31mA frase informada NÃO é um PALÍNDROMO\033[m')
