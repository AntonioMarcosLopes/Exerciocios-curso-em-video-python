from math import hypot

ca = float(input('DIgite o valor do cateto adjacente: '))
co = float(input('Digite o valor do cateto oposoto: '))

h = hypot(co, ca)

print(f'Um triangulo retangulo com catetos medindo {ca} e {co} tem sua hipotenusa como {h}')