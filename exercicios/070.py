total = mais_de_1000 = produtos = produto_mais_barato = 0
mais_barato = ''

while True:
    print('-'*40)
    print('Loja do jegue')
    print('-'*40)
    nome = str(input('Qual o nome do produto? '))
    preco = float(input('Qual o valor do produto? R$ '))
    total += preco
    produtos += 1
    if preco > 1000:
        mais_de_1000 += 1
    if produtos == 1:
        produto_mais_barato = preco
    elif preco < produto_mais_barato:
        produto_mais_barato = preco
        mais_barato = nome
    decisao = str(input('Quer continuar? [S/N] ')).strip().upper()
    if decisao in 'nN':
        break
    elif decisao in 'Ss':
        continue
    else:
        print('Valor invalido')
print(f"""A compra com o total de {produtos} produtos deu R${total:.2f}
Temos {mais_de_1000} produtos custando mais de R$ 1000.00
O produto mais barato é {mais_barato} custando R${produto_mais_barato:.2f}""")