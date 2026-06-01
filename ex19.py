'''
Uma empresa precisa automatizar o cálculo do salário líquido de seus funcionários com base no cargo 
que ocupam e nas deduções de impostos (INSS e IRRF). Escreva um programa em Python que receba o cargo de um
colaborador e realize os cálculos descritos a seguir.
'''

cargo = input("Qual é o seu cargo atual? ").lower()
if cargo == "caixa":
    sal = 1500
elif cargo == "vendedor":
    sal = 2400
elif cargo == "gerente":
    sal = 4000
else:
    print ("Não trabalha aqui")
    sal = 0
#print(sal)
inss = sal * 0.12
if sal > 2000:
    irrf = sal * 0.14
else:
    irrf = sal * 0.08
vinss = sal - inss
salf = vinss - irrf
print(f"Salário Inicial: {sal:.2f}")
print(f"Desconto INSS: {inss:.2f}")
print(f"Desconto IRRF: {irrf:.2f}")
print(f"Salário Líquido: {salf:.2f}")
