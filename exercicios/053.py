f = str(input('Digite uma frase ')).strip().upper()
palavras = f.split()
junto = ''.join(palavras)
inverso = junto[::-1]
# for letra in range(len(junto)-1, -1, -1):
    # inverso += junto[letra]
print(f'A frase {junto} invertida fica {inverso}')
if inverso == junto:
    print('É um palindromo')
else:
    print('A frase não é jum palindromo')