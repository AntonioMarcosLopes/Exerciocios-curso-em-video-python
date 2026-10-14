brasileirao = ('Flamengo', 'Palmeiras', 'Athletico-PR', 'Fluminense', 'Bahia', 'Cruzeiro', 'Atlético-MG', 'Santos', 'São Paulo', 'Coritiba', 'Bragantino', 'Vitória', 'Botafogo', 'Vasco', 'Mirassol', 'Corinthians', 'Internacional', 'Grêmio', 'Remo', 'Chapecoense',)

for pos, clube in enumerate(brasileirao):
    print(f'{pos+1}° {clube}')

g5 = brasileirao[0:5]
print('='*10,'G5 na tabela', '='*10)
for t in g5:
    print(t)

p4 = brasileirao[-4:]
print('='*10,'Zona de rebaixamento', '='*10)
for t in p4:
    print(t)

chapecoense = brasileirao.index('Chapecoense') + 1
print(f'Chapecoense está na posição {chapecoense}° na tabela')