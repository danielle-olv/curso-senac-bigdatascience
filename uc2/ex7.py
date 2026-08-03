itens_estoque = [12, 3, 8, 2, 15, 4, 20]
quantos_criticos = 0

for i in itens_estoque:
    if i<5:
        quantos_criticos+=1

print(f"Existem {quantos_criticos} produtos com estoque crítico (menos que 5)")