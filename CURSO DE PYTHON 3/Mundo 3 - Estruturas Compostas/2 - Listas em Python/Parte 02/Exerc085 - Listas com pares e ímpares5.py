''' 
 Exercício Python #085 - Listas com pares e ímpares:
 Crie um programa onde o usuário possa digitar sete valores numéricos 
 e cadastre-os em uma lista única que mantenha separados os valores 
 pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
'''
print("== Exercício Python #085 - Listas com pares e ímpares ==")
lista_geral = [[],[]]
for x in range(1,8):
    valor = int(input(f'{x}º valor: '))
    if valor % 2 == 0:
        lista_geral[1].append(valor)
    else:
        lista_geral[0].append(valor)
print('-'*56)
lista_geral[0].sort()
lista_geral[1].sort()
print(f"Números pares: {lista_geral[1]}")
print(f"Números ímpares: {lista_geral[0]}")
