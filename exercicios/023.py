numero = int(input('digite um numero: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print(f"""Analisando o numero {numero}
Unidade: {u}
Dezena: {d} 
Centena: {c}
Milhar: {m}""")
