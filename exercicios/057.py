sexo = str(input('Informe seu sexo: [M,F] ')).strip().upper()

while sexo not in 'MmFf':
    sexo = str(input('Valor invalido, favor digite de novo: ')).strip().upper()
print(f'Sexo {sexo} adiconado e validado com sucesso')