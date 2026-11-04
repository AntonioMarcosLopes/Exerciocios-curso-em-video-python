lista = []

while True:
    valor = int(input('Digite um valor: '))
    if valor in lista:
        print('Valor duplicado!! não vou adicionar ')
    else:
        lista.append(valor)
        print('Valor adiconado com sucesso...')
    resposta = str(input('deseja continuar? [S/N]: '))
    if resposta in 'Ss':
        continue
    elif resposta in 'Nn':
        break
    else:
        resposta = str(input('Resposta incoerente. Voce deseja continuar? [S/N] '))
        if resposta in 'Nn':
            break
lista.sort()
print(f'Os valores digitados foram: {lista}')