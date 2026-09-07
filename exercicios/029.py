velociade = int(input('Qual a velociade do carro? '))

if velociade > 80:
    multa = (velociade - 80) * 7
    print(f'O veiculo atingiu velociade acima da via a multa será de R${multa:.2f}')
else:
    print('O veiculo está na lei')