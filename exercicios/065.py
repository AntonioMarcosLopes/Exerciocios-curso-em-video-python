cont = maior = menor = s = 0
resposta = 'S'

while resposta in 'Ss':
    valor = int(input('Digite um valor: '))
    # adicionando os valores da quantidade de números e a soma deles para a media
    cont += 1
    s += valor
    # a partir do primeiro valor esse valor será o maior e menor inicial
    if cont == 1:
        maior = menor = valor
    # o proximo ser maior que o antigo ele será o novo maior
    if  valor > maior:
        maior = valor
    # o proximo ser menor que o antigo ele será o novo menor
    elif valor < menor:
        menor = valor
    # pergunta de ele quer continuar
    resposta = str(input('Quer continuar [s/n] ? ')).upper()
# aqui calcula a média
media = s / cont

print(f"""Com os dados recebidos temos {cont} numeros digitados onde sua média foi de: {media}
O menor valor foi: {menor}
O maior valor foi: {maior}""")