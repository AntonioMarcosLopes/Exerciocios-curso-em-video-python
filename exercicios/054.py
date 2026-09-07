maioridade = 0
menoridade = 0

for i in range(0, 7):
    p = int(input(f'Idade da {i+1}° pessoa: '))
    idade = 2025 - p
    if idade >= 21:
        maioridade += 1
    else:
        menoridade +=1
print(f'Temos {maioridade} pessoas adultas e {menoridade} pessoas para atingir a maioridade')
