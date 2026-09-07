cont = 0
s = 0
n = 0

while n != 999:
    n = int(input('Digite um valor [999 para sair]: '))
    if n != 999:
        s += n
        cont += 1
print(f'Você digitou {cont} números e a soma entre eles foi {s}.')