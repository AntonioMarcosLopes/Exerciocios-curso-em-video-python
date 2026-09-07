cidade = str(input('Fale o nome da sua cidade: ')).strip()
cidade_upper = cidade.upper()

if cidade_upper[:5] == 'SANTO':
    print(True)
else:
    print(False)