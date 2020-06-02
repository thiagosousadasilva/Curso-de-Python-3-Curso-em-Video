''' 
Exercício Python #079 - Valores únicos em uma Lista
Crie um programa onde o usuário possa digitar vários valores numéricos 
e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não 
será adicionado. No final, serão exibidos todos os valores únicos digitados, 
em ordem crescente. 
'''
print("== Exercício Python #079 - Valores únicos em uma Lista ==")
lista = []
while True:
    n = int(input('Digite o valor: '))
    escolha = input('Sair? [S/N]').upper()
    if n not in lista:
        lista.append(n)
    if escolha == 'S':
        break
lista.sort()
print('Os valores digitados foram: ', end=' ')
for valor in lista:
    print(valor, end=' ')