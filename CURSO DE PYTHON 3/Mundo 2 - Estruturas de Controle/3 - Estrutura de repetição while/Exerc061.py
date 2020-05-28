''' 
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros 
termos da progressão usando a estrutura while.
'''
print("=========== desafio 061============")
n1 = int(input('Informe o primeiro termo: '))
r = int(input('Informe a razão: '))
termo = n1
print('=-=' * 12)
x = 1
while x <= 10:
    if x == 1:
        print('01 -', termo)
    else:
        termo += r
        if x < 10:
            print('0'+str(x)+' -', termo)
        else:
            print(str(x)+' -', termo)
    x += 1