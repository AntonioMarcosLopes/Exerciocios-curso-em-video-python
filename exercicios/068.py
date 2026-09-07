from random import randint

vitoria = 0

while True:
    player = int(input('Vamos jogar par ou impar fale um número: '))
    escolha = str(input('Par ou impar [p/i] ')).strip().upper()
    comp = randint(0, 11)
    total = comp + player
    if total % 2 == 0:
        prorie = 'PAR'
    else:
        prorie = 'IMPAR'
    print(f'Você jogou {player} eu joguei {comp} o que dar {total} que é {prorie}')
    if escolha == 'P' and prorie == 'PAR' or escolha == 'I' and prorie == 'IMPAR':
        print(f'Você escolheu {prorie} e acertou!!')
        vitoria += 1
    elif escolha == 'P' and prorie == 'IMPAR' or escolha == 'I' and prorie == 'PAR':
        break
    else:
        print('valores invalidos')
print(f'Você perdeu depois de {vitoria} vitórias')