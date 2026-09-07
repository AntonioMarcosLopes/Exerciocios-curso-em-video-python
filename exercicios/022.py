nome = str(input('Digite seu nome: ')).strip()

mai = nome.upper()
minu = nome.lower()
letras = len(nome) - nome.count(' ')
pl = nome.find(' ')
separa = nome.split()


print(f""" Analisando seu nome...
Seu nome em maiúsculas é {mai}
Seu nome em minusculas é {minu} 
Quantidade de letras no seu nome é {letras} letras
Seu primeiro é {separa[0]} com {pl} letras""")