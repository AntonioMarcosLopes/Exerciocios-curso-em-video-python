casa = int(input('Qual o valor da casa? R$'))
salario = float(input('Qual é o seu salario? R$'))
anos = int(input('Em quantos ano voce quer pagar? '))

qprestacao = anos * 12
prestacao = casa / qprestacao
limite = salario * 0.30

print(f"""Para pagar uma case de R${casa} em {anos}anos a prestação mensal será de R${prestacao:.2f}""") 

if prestacao <= limite:
    print('Emprestimo pode ser CONCEBIDO!')
else:
    print('Emprestimo NEGADO') 