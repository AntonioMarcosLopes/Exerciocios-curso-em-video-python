from math import factorial

n = int(input('Digite um valor para usarmos seu fatorial: '))
f = factorial(n)
c = n
print(f'{n}! = ', end='')
while c > 0:
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1
print(f, end='')