tabela_de_preço = ( "Mouse Gamer", 89.90,
    "Teclado Mecânico", 199.90,
    "Monitor", 799.90,
    "Headset Gamer", 149.90,
    "Mousepad", 29.90,
    "Webcam HD", 119.90,
    "Pendrive 64GB", 39.90,
    "SSD 480GB", 249.90,
    "Memória RAM 8GB", 129.90,
    "Placa de Vídeo", 1499.90,
    "Processador Ryzen 5", 899.90,
    "Placa-Mãe", 599.90,
    "Fonte 600W", 279.90,
    "Gabinete Gamer", 349.90,
    "Cooler para Processador", 79.90,
    "Caixa de Som", 69.90,
    "Microfone USB", 159.90,
    "Notebook", 2999.90,
    "Cadeira Gamer", 899.90,
    "Roteador Wi-Fi", 189.90)

for i in range (0, len(tabela_de_preço), 2):
    item = tabela_de_preço[i]
    preco = tabela_de_preço[i + 1]
    print(f'{item:.<30} R${preco:.2f}')