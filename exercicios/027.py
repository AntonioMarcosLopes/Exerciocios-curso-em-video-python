nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()
u = n[len(n)-1]

print(f'Ola! Prazer te conhecer seu primeiro nome é {n[0]} e seu ultimo nome é {u}')