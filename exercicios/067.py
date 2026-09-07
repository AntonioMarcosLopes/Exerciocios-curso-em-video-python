

while True:
    print('-' * 40)
    n = int(input('Qual número voê quer a tabuada? '))
    print('-' * 40)
    if n > 0:
        for i in range (1,11):
            resul = n * i
            print(f'{n} x {i} = {resul}')
    if n < 0:
        break
    else:
        print('Todo numero multplicado por zero é zero')
print('Acabou pois o valor negativo')