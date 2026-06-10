#Desenvolva um código que leia um valor e calcule 10% sobre o valor
valor =  float(input("Informe um valor: "))
p =  float(input("Digite o valor da porcentagem: "))
#p = valor *10 / 100
tot = valor * p / 100
print(f"{p:.0f}% sobre o valor de {valor:.0f} é igual a {tot:.0f}")
