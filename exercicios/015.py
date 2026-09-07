dias = int(input('Quantos dias o carro ficou alugado? '))
km = float(input('Quantos km o carro andou? '))
valor = (dias * 60) + (km * 0.15)
print(f"""O carro foi alugado por: {dias} dias
e andou: {km}km
então o valor a ser pago é: R${valor:.2f} 
""")