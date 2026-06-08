senha_correta = "python123
tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas:
    tentativa = input(f"Digite a senha(tentativa{tentativa + 1}/{max_tentativas}):")
    if tentativa == senha_correta:
        print("Acesso concedido! Bem-vindo(a).")
        break
    else:
        print("Senha Incorreta")
        tentativas += 1   #+= significa tentativas = tentativas + 1
else:
    print("Acesso bloqueado")