#Desenvolva um código Python que leia um valor e mostre a tabuada desse valor usando for...
v = int(input("Digite um valor: "))
x = 1
while x <= 10:
    y = v * x
    print(f"{v} X {x} = {y}")
    x = x + 1