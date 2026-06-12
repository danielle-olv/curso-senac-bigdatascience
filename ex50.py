# Desenvolva um codigo pytjon que atraves de FUNCAO, o usuario digita um nome e ele sera impresso 10x

def repetir_nome(nome):
        for i in range(1,10):
            print(nome)
nome_user = input("Digite um nome: ")
repetir_nome(nome_user)
