preco = float(input('Qual o preço do produto? R$'))
pagamento = int(input('Para pagamento tem as seguintes opções:' \
'Cartão(1)' \
'À vista no dinheiro/cheque(2)' \
'À vista no cartão(3)' \
'Digite o numero da opção: '))

if pagamento == 1:
    parcela = int(input('Você irá querer em quantas parcelas? '))
    if parcela == 2:
        valor = preco/2
        print(f'Fica 2x de R${valor:.2f} cada')
    else:
        valor = (preco * 1.20)/parcela
        print(f'FIca {parcela}x de R${valor:.2f}')
elif pagamento == 2:
    desconto = preco * 0.9
    print(f'Como é à vista em dinheiro fica R${desconto:.2f}')
else:
    cartão = preco * 0.95
    print(f'Como é à vista no cartão fica R${cartão:.2f}')