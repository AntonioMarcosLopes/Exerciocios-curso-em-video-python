from random import choice

sorteio = int(input('Digite um número de 0 a 5: '))
lista = [0, 1, 2, 3, 4, 5]

escolhido = choice(lista)

if escolhido == sorteio:
    print('Parabens! Você acertou!')
else:
    print(f'Você errou! O valor certo é {escolhido}')