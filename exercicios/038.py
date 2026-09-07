v1 = int(input('Digite 0 valor 1: '))
v2 = int(input('Digite 0 valor 2: '))

if v1 > v2:
    print(f'O primeiro valor({v1}) é maior')
elif v2 > v1:
    print(f'O segundo valor({v2}) é maior')
elif v1 == v2:
    print('Os valores são iguais')