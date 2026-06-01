data = input("Que dia é hoje? ").lower()
hora = int(input("Que horas são agora? "))
if (data == "sexta") and (hora == 21):
    print("Sextou! Você merece um chopp")
elif (data == "sexta") and (hora >= 22) or (hora <= 5):
    print("Sextou! Você merece pelo menos dois chopps")
else:
    print("Ainda não sextou! Não saia da rotina e vá estudar!")