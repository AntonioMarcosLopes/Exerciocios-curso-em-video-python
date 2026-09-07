distancia = int(input('Quantos km tem a viagem? '))

if distancia > 200:
    valor = distancia * 0.45
    print(f'A viagem com {distancia}km vai custar R${valor:.2f}')
else:
    valor = distancia * 0.50
    print(f'A viagem com {distancia}km vai custar R${valor:.2f}')