from random import choice
from time import sleep

lista = list(range(0, 11))
escolhido = choice(lista)
escolha = 11
palpites = 0
while escolha != escolhido:
    escolha = int(input('Digite o numero que você pensou de 0 até 10: '))
    sleep(1)
    palpites += 1
    if escolha != escolhido:
        print('Suá escolha está errada tente denovo')
        sleep(1)
        if escolha > escolhido:
            print('Menos... ')
            sleep(1)
        elif escolha < escolhido:
            print('Mais...')
            sleep(1)
print(f'Parabens!! Você acertou o numero erá: {escolhido} com {palpites} palpites')