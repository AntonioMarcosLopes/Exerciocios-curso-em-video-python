lista = []

quant = int(input('Você quer digitar quantos numeros? '))

for i in range(0, quant):
    lista.append(int(input('Digite um valor para a lista ')))
print('='*30)
print (f"""Os valores digitados foram: {lista},
foram digitados {len(lista)} valores.""")

lista.sort(reverse=True)
print(f'os valores em ordem decrescente são: {lista}')

if 5 in lista:
    print(f'O valor 5 foi digitado {lista.count(5)} vezes')
else:
    print('valor 5 não foi encontrado na lista')