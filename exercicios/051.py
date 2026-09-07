a1 = int(input('Digite o primeiro termo '))
r = int(input('Dgite a razão '))

for i in range(1,11):
    termo = a1 + (i - 1) * r
    print (termo ,'-> ', end='')
print('Acabou')