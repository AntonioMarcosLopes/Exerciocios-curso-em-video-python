listanum = []
min = 0
max = 0

for n in range(0,5):
    listanum.append(int(input(f'digite um valor para a posição {n}: ')))
    if n == 0:
        min = max = listanum[n]
    else:
        if listanum[n] > max:
            max = listanum[n]
        elif listanum[n] < min:
            min = listanum[n]

for i, v in enumerate(listanum):
    if v == min:
        print(f'{i}...')

print(f"""{'='*30}
Voce digitou os valores)
{listanum}""")
print(f'o menor valor é {min} nas posições: ', end= '') 
for i, v in enumerate(listanum):
    if v == min:
        print(f'{i}...', end='')
print()
print(f'O maior valor é {max} nas posições: ', end= '')
for i, v in enumerate(listanum):
    if v == max:
        print(f'{i}...', end='')
print()
