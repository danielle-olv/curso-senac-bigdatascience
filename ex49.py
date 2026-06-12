'''
Desenvolva uma função em python que recebe a idade e o gênero de uma pessoa. 
Se a idade for maior ou igual a 18 e o gênero for masculino, imprima "apto a se alistar", caso contrário, imprima "não apto".
'''
print("Bem Vindo ao Portal de Alistamento Militar")
def apto (idade, gen):
    if idade >= 18 and gen == "M" :
        print("Você está apto para o alistamento")
    else :
        print ("Você não é apto para o alistamento")

gen = input("Digite o seu genero (M-masculino ou F-feminino): ").upper().strip()
idade = int(input("Digite sua idade: "))
apto(idade, gen)