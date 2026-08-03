fretes = [15.50, -2.00, 10.00, 25.00, -5.50, 30.00]

fretes_corrigidos = []

for i in fretes:
    if i >= 0:
        fretes_corrigidos.append(i)

print(fretes_corrigidos)