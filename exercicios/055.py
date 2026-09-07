p1 = float(input('Peso da 1° pessoa: '))
maiorpeso = p1
menorpeso = p1

for i in range(1,6):
    p = float(input(f'Peso da {i + 1}° pessoa: '))
    if p > maiorpeso:
        maiorfinal = p
    elif p < menorpeso:
        menorfinal = p
    else:
        maiorfinal = maiorpeso
        menorfinal = menorpeso
print(f"""O maior peso é {maiorfinal}kg
O menor peso {menorfinal}kg""")