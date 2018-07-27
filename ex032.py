from datetime import date
print('Se você digitar zero (0) será lido o ano da sua máquina')
ano = int(input('Me diga um ano: '))
if ano == 0:
    ano = date.today().year
if ano %4 ==0 and ano %100 !=0 or ano %400 ==0:
    print('O ano {} é Bissexto'. format(ano))
else:
    print('O ano {} não é Bissexto'.format(ano))