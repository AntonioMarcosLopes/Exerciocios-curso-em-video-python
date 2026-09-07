n = int(input('Digite um número: '))
total = 0
for i in range(1, n+1):
    if n % i == 0:
        print('\033[32m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print(i, end=' ')
print(f'\n\033[mO número {n} foi divisivel {total} vezes ')
if total == 2:
    print('Por isso ele é um número primo')
else:
    print('Por isso ele não é um número primo')