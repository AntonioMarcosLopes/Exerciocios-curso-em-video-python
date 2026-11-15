lista = []
par = []
impar = []

quant = int(input('Você quer digitar quantos numeros? '))

for i in range(0, quant):
    n = (int(input('Digite um valor para a lista ')))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
print(f"""Os numeros dgitados foram: {lista},
Os números pares foram: {par}
e os impares foram: {impar}""")