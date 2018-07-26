from random import  choice
aluno1 = str(input('Digite nome do aluno: '))
aluno2 = str(input('Digite nome do aluno: '))
aluno3 = str(input('Digite nome do aluno: '))
aluno4 = str(input('Digite nome do aluno: '))
lista =  [aluno1, aluno2, aluno3, aluno4]
sorteio = choice(lista)
print('O sorteado foi {}!!!'.format(sorteio))