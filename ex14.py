"""
5) Desenvolva um código Python que leia uma idade e seguindo a lógica real da vida imprima
se é menor de idade, maior de idade ou idoso.
"""
idad = int(input("Quantos anos você tem? "))
if idad < 18:
    print(f"Com {idad} anos você ainda é menor de idade.")
elif idad >= 60:
    print(f"Com {idad} anos você já é um(a) idoso(a)")
else:
    print(f"Com {idad} você já é maior de idade")