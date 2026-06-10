def imposto(x, y):
    return x * y
imp = float(27.5 / 100)

print("Vamos calcular o seu imposto de renda, bebê!")
salario = float(input("Digite o seu saláro bruto: "))

calc = imposto(imp, salario)
print(f"O seu imposto de renda para o salário de R${salario} infelizmente é R${calc:.2f}!")