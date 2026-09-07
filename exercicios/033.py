v1 = int(input('Valor 1 '))
v2 = int(input('Valor 2 '))
v3 = int(input('Valor 3 '))

meno = v1
if v2<v1 and v2<v3:
    meno = v2
if v3<v1 and v3<v2:
    meno = v3

maior = v1
if v2>v1 and v2>v3:
    maior = v2
if v3>v1 and v3>v2:
    maior = v3

print(f'O maior valor é {maior} e o menor valor é {meno}')
