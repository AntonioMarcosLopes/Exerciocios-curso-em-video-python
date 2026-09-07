a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a < b + c and b < a + c and c < a + b:
    print('Os segmentos podem formar um triangulo')
    if a == b and b == c:
        print('É um triangulo equilatero')
    elif a == b or b == c or c == a:
        print('É um triangulo isósceles')
    else:
        print('É um triangulo escaleno')
else:
    print('Os segmentos não podem formar um triangulo')
