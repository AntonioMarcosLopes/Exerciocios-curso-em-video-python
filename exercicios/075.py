lista = (int(input('Digite primeiro valor: ')),
        int(input('Digite segundo valor: ')),
        int(input('Digite terceiro valor: ')),
        int(input('Digite quarto valor: ')))

print(f'Você digitou os valores :{lista}')

print(f'O numero 9 aparece {lista.count(9)} vezes')

print(f'P primeiro valor 3 foi digitado na posição {lista.index(3) + 1}')

for item in lista:
    if item % 2 == 0:
        print(f'{item} é par')