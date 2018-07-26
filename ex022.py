frase = ('    Ricardo Santiago Roberto Junior   ')
#Cortes na frase
print(8)
print(frase[:9])
print(frase[9:15])
print(frase[9:20:3])
#Tamanho da frase
print(len(frase))
#Fragmentando a frase
print(frase.split())
frase1 = frase.split()
#Unindo frase fragmentada
print('-'.join(frase1))
#Substituindo palavras dentro da string
frase = frase.replace('Ricardo', 'Adailson')
print(frase)