expressao = str(input('Digite aqui uma expressão: '))
pilha = []

for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        pilha.append(')')

abertos = pilha.count('(')
fechados = pilha.count(')')

if abertos == fechados:
    print('Sua equação é valida')
else:
    print('Sua equação não é valida')