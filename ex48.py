'''
1) Crie uma função que calcule o IMC
Menor que 18,5 Magreza
18,5 a 24,9    Normal
25 a 29,9      Sobrepeso
30 a 34,9      Obesidade grau I
35 a 39,9      Obesidade grau II
Maior que 40   Obesidade grau III

imc = peso / (altura * altura)
'''
def imc(p,a):
    x = p / (a * a)
    if (x < 18.5):
        print(f"O valor do seu IMC é: {x:.2f}")
        print("Menor do que 18,5 - Magreza")
    elif (x > 18.5) and (x < 24.9):
        print(f"O valor do seu IMC é: {x:.2f}")
        print("Entre 18,5 a 24,9 - Normal")
    elif (x > 25) and (x < 29.9):
        print(f"O valor do seu IMC é: {x:.2f}")
        print(f"Entre 25 a 29,9 - Sobrepeso")
    elif (x > 30) and (x < 34.9):
        print(f"O valor do seu IMC é: {x:.2f}")
        print(f"IMC entre 30 a 34,9 - Obesidade grau I")
    elif (x > 35) and (x < 39.9):
        print(f"O valor do seu IMC é: {x:.2f}")
        print(f"IMC entre 35 a 39,9 - Obesidade grau II")
    else:
        print(f"O valor do seu IMC é: {x:.2f}")
        print(f"IMC maior que 40   Obesidade grau III")

peso=float(input("Informe o seu peso atual: "))
altura=float(input("Informe a sua altura atual (Utilize ponto final no lugar da vírgula): "))
imc(peso,altura)

