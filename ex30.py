#Desenvolva um código Python que leia um valor e mostre a tabuada desse valor usando for...
num = int(input("Você quer saber a tabuada de qual número inteiro? "))
for i in range (1,11):
    val = num * i 
    print (f"{num} x {i} = {val}")
print(f"Esta é a tabuada do número {num}")
    