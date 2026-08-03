#{"id": 0 , "nome": "", "preco": 0.0, "estoque": 0}
produtos_db =  [{"id": 1 , "nome": "Teclado Mecânico Gamer", "preco": 150.00, "estoque": 15},
                {"id": 2 , "nome": "Monitor Samgung", "preco": 400.00, "estoque": 5},
                {"id": 3 , "nome": "Memória RAM 16gb", "preco": 1000.00, "estoque": 6}
                ]

carrinho = []

def buscar_produto(id_busca):

    for i in produtos_db:
        if id_busca == i["id"]:
            return i

    return None

while True:
    opcao = input("Digite: \n[0] Finalizar Compra \n[1] Procurar um item\n --> ")

    if opcao == "0":
        print(carrinho)
        valor_final = 0
        for i in carrinho:
            valor_final += i['preco'] * i['estoque']
        print(f"Sua compra deu R${valor_final:.2f}")
        break
    elif opcao =="1":
        item_encontrado = None
        while item_encontrado == None:
            id_procurado = int(input("Digite o ID do item desejado:\n --> "))
            item_encontrado = buscar_produto(id_procurado)
            if item_encontrado == None:
                print("Item não encontrado, tente novamente")
            else:
                print(f"{item_encontrado["nome"] }| Preço: R${item_encontrado["preco"]:.2f}")
                if input("Você deseja adicionar ao carrinho? S/N").upper() == "S":
                    quantidade = int(input("Quantas unidades deseja adicionar?"))
                    if item_encontrado["estoque"] < quantidade:
                        print("Estoque insuficiente")
                    else:
                        item_encontrado['estoque'] = quantidade
                        carrinho.append(item_encontrado)
                        #CONFERIR:
                        #for i in produtos_db:
                            #if i['id'] == id_procurado:
                                #i['estoque'] -= quantidade


    else:
        print("Opção inválida, tente novamente")