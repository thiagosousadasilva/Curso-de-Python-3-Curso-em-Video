# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de
#tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
print("=========== desafio 011 ============")
largura = float(input('Informe a larguda da parede em metros: '))
altura = float(input('Informe a altura da parede em metros: '))
area = largura * altura
tinta = area / 2
print('A área de uma parede com {}m de largura e {}m de altura corresponde a {:.2f}m².'.format(largura, altura, area))
print('A tinta necessária para pintar {:.2f}m² são {:.2f} litros.'.format(area, tinta))