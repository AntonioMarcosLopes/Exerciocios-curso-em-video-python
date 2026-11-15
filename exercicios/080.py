lista = []
for i in range(0,5):
    n = int(input('Digite um valor: '))
    if i == 0  or n > lista[len(lista)-1]:
        lista.append(n)
        #para adicionar o primeiro valor
        #checar que se caso for o maior valor ir pro final da lista
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print(f'os valores digitados são: {lista}')