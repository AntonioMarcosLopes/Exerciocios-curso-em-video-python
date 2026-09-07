numero = int(input('Digite um numero: '))
converssor = int(input("""Voce tem essas opções para conversão:
1 para binario
2 para octal
3 para hexadecimal
digite qual opção quer: """))

if converssor == 1:
    binario = bin(numero)[2:]
    print(f'O numero {numero} em binario é {binario}')
elif converssor == 2:
    octal = oct(numero)
    print(f'O numero {numero} em octal é {octal}')
elif converssor == 3:
    hexa = hex(numero)
    print(f'O numero {numero} em hexadecimal é {hexa}')