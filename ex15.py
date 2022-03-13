from math import hypot 
cateto_oposto = float(input('Informe o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Informe o comprimento do cateto adjacente: '))

hipotenusa = hypot(cateto_oposto, cateto_adjacente)

print('O comprimento da hipotenusa é {:.2f}'.format(hipotenusa))