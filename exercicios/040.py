nota1 = int(input('Digite a sua primeira nota '))
nota2 = int(input('Digite a sua segunda nota '))

media = (nota1 + nota2)/2
print(f'Sua media é {media}')

if media >= 7:
    print('Aprovado')
elif media > 5:
    print('Recuperção')
else:
    print('Reprovado')