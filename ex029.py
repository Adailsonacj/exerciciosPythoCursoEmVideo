velocidade = float(input('Qual é a velocidade atual? '))
if velocidade > 80:
    print('Excedeu o limite de velocidade!')
    multa = (velocidade-80)*7
    print('Você deve pagar multa de R${:.2f}!'.format(multa))
else:
    print('Está dentro do limite permitido.')
