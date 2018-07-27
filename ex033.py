numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite um segundo número: '))
numero3 = int(input('Digite um terceiro número: '))
menor = numero1
if numero2 < numero1 and numero2 < numero3:
    menor = numero2
if numero3 < numero1 and numero3 < numero2:
    menor = numero3
maior = numero1
if numero2>numero1 and numero2>numero3:
    maior = numero2
if numero3>numero1 and numero3>numero2:
    maior = numero3

print('O meno número é {} e o maior é {}'.format(menor, maior))
