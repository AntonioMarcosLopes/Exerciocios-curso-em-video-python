homem_mais_velho = 0
mulheres_mais_novas = 0
media_idade_grupo = 0
s = 0

for i in range(1, 5):
    nome = str(input(f'Nome {i}° pessoa: '))
    idade = int(input(f'Idade da {i}° pessoa: '))
    sexo = int(input(f'Sexo da {i}° pessoa 1 para feminino 2 para masculino: '))
    # parte da quantidade de mulheres com menos de 20 anos
    if sexo == 1 and idade < 20:
        mulheres_mais_novas += 1
    # parte que define o homem maisvelho e captura seu nome e idade
    elif sexo == 2:
        if idade > homem_mais_velho:
            homem_nome_velho = nome
            homem_mais_velho = idade
    # parte da media das idades
    s += idade
media = s/4
print(f"""Com o final da analise temos que:
A média de idade do grupo é {media}
Mulheres abaixo de 20 anos temos {mulheres_mais_novas}
O homem mais velho seu nome é: {homem_nome_velho} e sua idade é: {homem_mais_velho}""")