base_usuarios = [
{"id": 101, "nome": "Alice"},
{"id": 102, "nome": "Bruno"},
{"id": 103, "nome": "Carla"},
]

encontrado = False
busca_id = int(input("Digite o ID procurado: "))

for i in base_usuarios:
    if busca_id==i["id"]:
        encontrado=True
        print(i["nome"])


if not encontrado:
    print("Nenhum usuário com esse ID foi encontrado")