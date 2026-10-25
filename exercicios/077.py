palavras = ('Casa','Livro','Mesa','Cadeira','Computador','Teclado','Mouse','Monitor','Celular','Garrafa','Janela','Porta','Sapato','Camisa','Mochila','Caneta','Papel','Relogio','Quadro','Fone')

for p in palavras:
    print(f'\nNa palavra {p.upper} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end = ' ')