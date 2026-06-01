'''
2) Desenvolva um código em Python que leia o ano de nascimento e o ano atual,
calcule a idade, se a idade for maior igual a 18 imprimir a mensagem "maior de idade"
senão imprimir "menor de idade"
'''
an = int(input("Informe o seu ano de nascimento: "))
aa = int(input("Informe o ano atual: "))
ida = aa - an
if (ida >= 18):
    print(f"Com {ida} você já é maior de idade.")
else:
    print(f"Com {ida} você ainda é menor de idade.")
