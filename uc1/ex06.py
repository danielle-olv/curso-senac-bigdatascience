#Desenvolva um código que leia o ano de nascimento e no final mostre sua idade
anasc = int(input("Em qual ano você nasceu? "))
aatu = int(input("Informe o ano atual: "))
idad = aatu - anasc
#print("Atualmente você tem ",idad," anos.")
print(f"Você tem {idad} anos e nasceu em {anasc}") #boa prática em programação python