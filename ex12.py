"""
3) Desenvolva um código que digite um nome de usuário,
se o nome for "SENAC", imprimir "Seja bem vindo Senac", 
senão imprimir "Usuário nome_dele não cadastrado"
"""
nuser = input("Digite o seu nome: ").lower()
if (nuser == "senac"):
    print("Seja bem-vindo, SENAC")
else:
    print(f"Usuário {nuser} não cadastrado")