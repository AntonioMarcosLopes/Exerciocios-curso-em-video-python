import random

rodadas = 9
while rodadas > 0:
    escolhido = str(input('Vamos jogar pedra papel tesoura escolha: '))

    escolhas = ['pedra','papel','tesoura']
    resposta = random.choice(escolhas)

    if escolhido == 'papel':
        if resposta == 'pedra':
            print(f'Você ganhou {escolhido} ganha de {resposta}')
        elif resposta == 'papel':
            print(f'Empate! nós dois escolhemos {resposta}')
        elif resposta == 'tesoura':
            print(f'Você perdeu! {resposta} ganha de {escolhido}')
    elif escolhido == 'pedra':
        if resposta == 'tesoura':
            print(f'Você ganhou {escolhido} ganha de {resposta}')
        elif resposta == 'pedra':
            print(f'Empate! nós dois escolhemos {resposta}')
        elif resposta == 'papel':
            print(f'Você perdeu! {resposta} ganha de {escolhido}')
    elif escolhido == 'tesoura':
        if resposta == 'papel':
            print(f'Você ganhou {escolhido} ganha de {resposta}')
        elif resposta == 'tesoura':
            print(f'Empate! nós dois escolhemos {resposta}')
        elif resposta == 'pedra':
            print(f'Você perdeu! {resposta} ganha de {escolhido}')
    rodadas = rodadas-1
    print(f'O número de rodade é: {rodadas} vamos continuar jogando!!')