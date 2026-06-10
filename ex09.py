val = float(input("Digite um valor: "))
porcentagem = int(input("Digite a porcentagem (ex: 15): "))
resultado = val * (porcentagem / 100)
print(f"{porcentagem}% de {val} é {resultado:.0f}")