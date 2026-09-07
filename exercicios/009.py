numero = int(input('Digite um numero'))
tabuada = 1

print('='*10)
while tabuada < 11:
    produto = numero * tabuada
    print(f'{numero} * {tabuada} = {produto}')
    tabuada = tabuada + 1
print('='*10)