s = 0
count = 0

for i in range(0, 6):
    num = int(input('digite um numero: '))
    if num % 2 == 0:
        s += num
        count += 1
print(f'A somataria entre os valores pares são {s} com {count} valores usados')