''' 
Exercício Python #082 - Dividindo valores em várias listas:
Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores 
pares e os valores ímpares digitados, respectivamente. 
Ao final, mostre o conteúdo das três listas geradas.
'''
print("== Exercício Python #082 - Dividindo valores em várias listas: ==")
lista = [] 
pares = []
impares = []
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    if valor % 2 == 0 and valor != 0:
        pares.append(valor)
    if valor % 2 != 0:
        impares.append(valor)
    escolha = input('Sair? [S/N]: ')
    if escolha in 'Ss':
        break
print('-'*40)
print(f'- Lista geral: {lista}')
if len(pares) > 0:
    print(f'- Lista pares: {pares}')
else:
    print('- Não foram digitados números pares.')
if len(impares) > 0:
    print(f'- Lista ímpares: {impares}')
else:
    print('- Não foram digitados números ímpares.')      
print('-'*40)  