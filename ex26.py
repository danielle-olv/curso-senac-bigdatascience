for i in range(0,5):
    x = int(input("Digite um número: "))
    y = x % 2
    if y == 1:
        print(f"{x} é um número impar")
    else:
        print(f"{x} é um número par")