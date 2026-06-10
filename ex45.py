def somar(a, b):
    return a + b
def subtrair(a, b):
    return a - b
def multi(a, b):
    return a * b
def divi(a, b):
    if b!=0:
        return a / b
    else:
        print("Valor inválido")
escolha = ""
while escolha != 0:
    escolha = input("digite uma opção: 1 - somar  2 - Subtrair  3 - Multiplicar  4 - Dividir ")
    num1 = int(input("Digite o primeiro número "))
    num2 = int(input("Digite o segundo número "))
    if escolha == "1":
        x = somar(num1, num2)
    elif escolha == "2":
        x = subtrair(num1, num2)
    elif escolha == "3":
        x = multi(num1, num2)
    else:
        x = divi(num1, num2)
    print(f"o resultado da operação é: {x}")
else:
    print("Operação terminada.")