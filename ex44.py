def adivinha(x, y):
    return f"{x}{y}"

print("Eu adivinho qual é o seu nome, sabia?")
nome = input("Digite aqui o seu nome que eu vou adivinhar: ")

mensagem = "Seja bem-vindo, "
resposta = adivinha(mensagem, nome)
print(resposta)