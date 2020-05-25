''' 
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- média abaixo de 5.0: reprovado.
- média entre 5.0 e 6.9: recuperação.
- média 7.0 ou superior: aprovado.
'''
print("=========== desafio 040============")
nt1 = float(input('Informe a primeira nota: '))
nt2 = float(input('Informe a segunda nota: '))
media = (nt1+nt2)/2
if media < 5:
    print('Média {:.1f} abaixo de 5.0: reprovado.'.format(media))
elif media >= 5 and media <= 6.9:
    print('Média {:.1f} entre 5.0 e 6.9: recuperação.'.format(media))
else:
    print('Média {:.1f} igual ou superior a 7.0: aprovado.'.format(media))