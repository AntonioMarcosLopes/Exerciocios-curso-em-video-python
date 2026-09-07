a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a < b + c and b < a + c and c < a + b:
    print('Os segmentos podem formar um triangulo')
else:
    print('Os segmentos não podem formar um triangulo')
