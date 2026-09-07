pessoas_18_mais = homens = mulheres_menos_20 = 0
pessoa = 1

while True:
    print('-' * 40)
    print(f'<---CADASTRO DA {pessoa}° PESSOA --->')
    print('-' * 40)
    idade = int(input('Idade da pessoa: '))
    sexo = str(input('Sexo da pessoa [M/F]: ')).strip().upper()
    pessoa += 1
    if idade >= 18:
        pessoas_18_mais += 1
    if sexo in 'fF' and idade < 20:
        mulheres_menos_20 += 1
    elif sexo in 'mM':
        homens += 1
    decisão = str(input('Quer continuar ? [S/N] ')).strip().upper()
    if decisão in 'sS':
        continue
    elif decisão in 'nN':
        break
    else:
        print('Valor invalido')
        continue
print(f"""Com a coleta de dados de {pessoa} pessoas temos:
Mulheres com idade menor que 20 anos: {mulheres_menos_20}
Pessoas com mais de 18 anos: {pessoas_18_mais}
Quantidade de homens cadastrados: {homens}""")