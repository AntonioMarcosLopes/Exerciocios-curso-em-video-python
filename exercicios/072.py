numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quize', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    user_numero = int(input('Digite um valor de 0 a 20: '))

    if user_numero >= 0  and user_numero <= 20:
        print(f'O número que você digitou é: {numeros[user_numero]}')
        resposta = str(input('Quer continuar? [S/N] ')).strip()
        if resposta in 'Ss':
            continue
        else:
            break
    else:
        print('Tente novamente.', end=' ')
