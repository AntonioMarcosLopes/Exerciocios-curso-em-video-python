import math

x = float(input('Digite um angulo: '))

sen = math.sin(math.radians(x))
cos = math.cos(math.radians(x))
tan = math.tan(math.radians(x))

print(f"""Dado o angulo {x}:
Seno: {sen:.2f}
Cosseno: {cos:.2f}
Tangente: {tan:.2f}""")