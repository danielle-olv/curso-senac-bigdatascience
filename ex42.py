'''
Desenvolva um código python que crie uma função que calcule o imc de uma pessoa. 
O usuário deve digitar o peso e a altura
'''
def imc(p, a):
    return p / (a * a) #imc = peso / (altura * altura)

peso = float(input("Informe o seu peso: "))
altura = float(input("Informe a sua altura: (use ponto em vez de vírgula)"))
tot = imc(peso, altura)
print(f"Seu índice de Massa Corporal é igual a {tot:.2f}")