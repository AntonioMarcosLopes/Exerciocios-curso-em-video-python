print('-'*22)
print('SEQUENCIA DE FIBONACCI')
print('-'*22)
n = int(input('Quantos digitos da sequencia quer mostrar? '))
t1 = 0
t2 = 1
print('~'*22)
print(f'{t1} -> {t2}', end='')
i = 3
while i <= n:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    i += 1
print(' -> FIM')