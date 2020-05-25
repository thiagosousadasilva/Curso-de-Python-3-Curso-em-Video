''' 
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10
primeiros termos dessa progressão.
'''
print("=========== desafio 051============")
n1 = int(input('Informe o primeiro termo: '))
r = int(input('Informe a razão: '))
termo = n1
print('=-=' * 12)
for x in range (1, 11):
    if x == 1:
        print('01 -', termo)
    else:
        termo *= r
        if x < 10:
            print('0'+str(x)+' -', termo)
        else:
            print(str(x)+' -', termo)