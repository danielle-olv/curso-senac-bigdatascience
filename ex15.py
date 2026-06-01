"""
6) Você foi contratado pelo governo para criar um sistema de
alistamento militar onde apenas está apto para o alistamento pessoas com
18 ou mais e do sexo masculino.
"""
idad = int(input("Quantos anos você tem? "))
gen = input("Qual é o seu gênero? (M/F) ").upper()
if (gen == "M") and (idad >= 18) and (idad <= 40):
    print ("Você cumpre os requisitos e pode se alistar.")
else:
    print("Você não cumpre os requisitos e não poderá se alistar")