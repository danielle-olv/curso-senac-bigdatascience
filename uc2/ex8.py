estoque = [{"id": 1, "nome": "Mochila", "quantidade": 4, "preco": 289.90},
           {"id": 2, "nome": "Boné", "quantidade": 15, "preco": 50.00},
           {"id": 3, "nome": "Casaco", "quantidade": 7, "preco": 149.90},
           ]

patrimonio_total = 0

for i in estoque:
    patrimonio_total += i["quantidade"] * i["preco"]
    # patrimonio_total = patrimonio_total + (i["quantidade"] * i["preco"])

print(f"Patrimonio total da empresa é de: R${patrimonio_total:.2f}")