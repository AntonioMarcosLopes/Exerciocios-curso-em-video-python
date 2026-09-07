idade = int(input('Digite sua idade '))

print('Sua categoria é: ')

if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JÚNIOR')
elif idade <= 25:
    print('SÊNIOR')
elif idade > 25:
    print('MASTER')


