a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))

i = 1

while i != 11:
    termo = a1 + (i - 1) * r
    print(termo,'-> ', end='')
    i += 1
print('Acabou')