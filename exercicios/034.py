salario = float(input('Digite aqui seu salario '))

if salario <= 1250:
    novo_salrio = salario * 1.15
    print(f'Seu salario com o ajuste é de R${novo_salrio:.2f}')
else:
    novo_salrio = salario * 1.10
    print(f'Seu salario com o ajuste é de R${novo_salrio:.2f}')