''' 
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.
'''
print("=========== desafio 056============")
grupoM = []   #grupo masculino
grupoF = []   #grupo feminino
idadeG = 0    #idade geral
IdadeM = 0    #idade mulheres
for x in range(1, 5):
    print('{} - Informe: '.format(x))
    nome = input('- Nome: ')
    idade = int(input('- Idade: '))
    sexo = int(input('- Sexo (0 - Fem / 1 - Masc): '))
    idadeG += idade
    print('')

    if sexo == 0:
        grupoF.append([idade, nome])
        if idade < 20:
            IdadeM += 1        
    else:
        grupoM.append([idade, nome])

grupoF.sort()   #Ordena a lista por idade
grupoM.sort()   #Ordena a lista por idade

print("=*=" * 15)
print(idadeG/4, 'É a média de idade do grupo.')
print(grupoM[len(grupoM)-1][1].capitalize(), 'é o homem mais velho.')
print(IdadeM, 'mulher(es) com menos de 20 anos.')
print("=*=" * 15)