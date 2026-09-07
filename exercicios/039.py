ano = int(input('Em qual ano você nasceu? '))
idade = 2025 - ano

print(f"Você nascido em {ano} tem {idade}anos")



if idade == 18:
    print('Faça o alistamneto imediatamente!!!')
elif idade > 18:
    ano_alistamento = idade - 18
    alistamento = 2025 - ano_alistamento
    print(f'Voce deveria ter se alistado no ano {alistamento}')
elif idade < 18:
    ano_alistamento = 18 - idade
    alistamento = 2025 + ano_alistamento
    print(f'Voce deverá se alistar no ano {alistamento}')