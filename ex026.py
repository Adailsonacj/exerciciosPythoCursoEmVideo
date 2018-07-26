frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase. \n A primeira ocorrência '
      'de "A" é na posição de número {}. \n A ultima ocorrência de "A"'
      ' é na posição de número {}'.format(frase.count('A'), frase.find('A')+1, frase.rfind('A')+1))
