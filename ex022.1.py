nome = input('Digite seu nome: ').strip()
nome1 = nome.split()
print('Seu nome em caixa alta: '+nome.upper())
print('Seu nome em caixa baixa: '+nome.lower())
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras. '.format(nome.find(' ')))
print('Seu primeiro nome tem {} letras. '.format(len(nome1[0])))