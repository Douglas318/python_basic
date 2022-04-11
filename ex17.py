from random import randint

aluno1 = (input('Informe seu nome: '))
aluno2 = (input('Informe seu nome: '))
aluno3 = (input('Informe seu nome: '))
aluno4 = (input('Informe seu nome: '))

sorteio = randint(1, 4)
print('O aluno sorteado foi o: {}'.format(sorteio))