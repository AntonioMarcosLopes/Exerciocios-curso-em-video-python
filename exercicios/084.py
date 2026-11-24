cadastros = list()
pessoas = list()
maispesos = list()
menospesos = list()
maispes = menospes = 0



while True:
    nome = str(input('Nome: '))
    peso = int(input('Peso: '))

    pessoas.append(nome)
    pessoas.append(peso)
    cadastros.append(pessoas[:])
    pessoas.clear()
    
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resposta == 'N':
        break


maispes = max(pessoas[1] for pessoas in cadastros)
menospes = min(pessoas[1] for pessoas in cadastros)

for pessoa in cadastros:
    if pessoa[1] == maispes:
        maispesos.append(pessoa[0])
    if pessoa[1] == menospes:
        menospesos.append(pessoa[0])    

print(f"""Quantidade de pessoas cadastradas: {len(cadastros)};
Maior peso é {maispes}kg a(s) pessoa(s) com ele são: {maispesos};
Menor peso é {menospes}kg a(s) pessoa(s) com ele são: {menospesos}""")