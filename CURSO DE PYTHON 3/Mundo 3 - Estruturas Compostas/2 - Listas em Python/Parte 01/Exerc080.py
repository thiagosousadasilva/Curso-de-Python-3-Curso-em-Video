''' 
 Exercício Python #080 - Lista ordenada sem repetições:
 Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma 
 lista, já na posição correta de inserção (sem usar o sort()). 
 No final, mostre a lista ordenada na tela.
'''
print("== Exercício Python #080 - Lista ordenada sem repetições ==")
lista = []
for x in range(1,6):
    valor = int(input(f'{x}º valor: '))
    if x == 1 or valor > lista[-1]:
        lista.append(valor)
    else:
        pos = 0 #posição
        while pos < len(lista):
            if valor <= lista[pos]:
                lista.insert(pos, valor)
                break
            pos += 1      
print(lista)