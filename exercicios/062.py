a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite o a razão: '))

termo = a1
i = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while i <= total:
        termo = a1 + (i - 1) * r
        print(termo,'-> ', end='')
        i += 1
    print('PAUSA')
    mais = int(input('Quantos termos quer mostrar a mais? '))
print('Fim')
print(f'Foi mostrado {total} termos ')