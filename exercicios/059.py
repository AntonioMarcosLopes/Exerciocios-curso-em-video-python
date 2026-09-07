from time import sleep

a = int(input('Valor 1: '))
b = int(input('Valor 2: '))

menu = 0
print('<---MENU--->')
while menu != 7:
    menu = int(input("""Aqui esta o menu e essa são suas escolhas:
    [1] somar
    [2] subtração
    [3] multiplicação
    [4] divisão
    [5] comparação
    [6] novo numero
    [7] sair do programa
    Qual sua escolha? """))

    if menu == 1:
        soma = a + b
        print(f'{a} + {b} = {soma}')
        sleep(2)
    elif menu == 2:
        subtração = a - b
        print(f'{a} - {b} = {subtração}')
        sleep(2)
    elif menu == 3:
        multiplicação = a * b
        print(f'{a} * {b} = {multiplicação}')
        sleep(2)
    elif menu == 4:
        divisão = a / b
        print(f'{a} / {b} = {divisão}')
        sleep(2)
    elif menu == 5:
        if a < b:
            print(f'{a} é menor que {b}')
            sleep(2)
        elif a > b:
            print(f'{a} é maior que {b}')
            sleep(2)
        else:
            print(f'os dois são iguais')
            sleep(2)
    elif menu == 6:
        a = int(input('Digite o novo valor1: '))
        b = int(input('Digite o novo valor2: '))
        sleep(2)
    elif menu == 7:
        print('Fechando programa...')
        sleep(2)
    else:
        print('Valor invalido tente novamente')
        sleep(2)
print('programa FINALIZADO')