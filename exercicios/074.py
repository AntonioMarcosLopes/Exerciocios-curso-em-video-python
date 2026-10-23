from random import randint

numeros = (randint(1,10), randint(1,10), randint(1,10),randint(1,10),randint(1,10))

print('Valor da sequência aleatória')

for n in numeros:
    print(n)

print(f"""Maior número da sequência: {max(numeros)}
Menor número da seqência: {min(numeros)}""")