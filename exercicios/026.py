frase = str(input('Digite uma frase: ')).strip()
pfrase = frase.upper()
a = pfrase.count('A')
f = pfrase.find('A') + 1
pf = pfrase.rfind('A') + 1

print(f'A letra a aparece {a} vezes a aparacendo a primeira vez na posição {f} e a ultima vez na posição {pf}')
