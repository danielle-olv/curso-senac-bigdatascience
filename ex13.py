"""
4) Desenvolva um código em Python que leia dois valores e mostre qual o maior entre eles.
"""

v1 = float(input("Digite o 1º valor: "))
v2 = float(input("Digite o 2º valor: "))
if (v1 > v2):
    print(f"O maior valor é o {v1:.0f}")
elif (v2 > v1):
    print(f"O maior valor é o {v2:.0f}")
else:
    print("Os dois números são iguais")