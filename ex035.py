seg1 = int(input('Digite um numero: '))
seg2 = int(input('Digite um numero: '))
seg3 = int(input('Digite um numero: '))

if seg1<(seg2+seg3) and seg2<(seg1+seg3) and seg3<(seg1+seg2):
    print('Os segmentos acima PODEM formar um triangulo')
else:
    print('\033[1;31;40mOs segmentos acima NÂO PODEM formar um triangulo\033[m')