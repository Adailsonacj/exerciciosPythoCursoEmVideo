nome = str(input('Digite seu nome: ')).strip()
n = nome.split()
print('Seu primeiro nome é {} e seu ultimo nome é {}'.format(n[0], n[len(n)-1]))
