''' 
Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. 
O programa encerra quando ele disser que quer mostrar 0 termos.
'''
print("=========== desafio 062============")

n1 = int(input('Informe o primeiro termo: '))
r = int(input('Informe a razão: '))

termo = n1
print('===' * 12)
inicio = 1
fim = 11
y = 1
while y != 0:
    for x in range(inicio, fim):
        print('\033[34m', end='')
        if x == 1:
            print('01 -', termo)
        else:
            termo += r
            if x < 10:
                print('0'+str(x)+' -', termo)
            else:
                print(str(x)+' -', termo)
        
        print('\033[m', end='')
        
        x += 1
        inicio += 1

    print('---> PAUSE <---')

    y = int(input('Quantos termos você quer mostrar a mais? '))
    if y != 0:
        fim += y
print('Fechando...')