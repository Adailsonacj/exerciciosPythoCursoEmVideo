from random import shuffle
aluno1 = str(input('Digite nome do aluno: '))
aluno2 = str(input('Digite nome do aluno: '))
aluno3 = str(input('Digite nome do aluno: '))
aluno4 = str(input('Digite nome do aluno: '))
lista =  [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print('S ordem de apresentação é: ')
print(lista)