import pandas as pd
# Criando um dataset de vendas simples
dados = {
    'ID_Pedido': [1001, 1002, 1003, 1004, 1005, 1006, 1007],
    'Produto': ['iPhone 14', 'Mouse Gamer', 'MacBook Air', 'Teclado Mecânico', 'Monitor 24', 'iPhone 14', 'Mouse Gamer'],
    'Categoria': ['Celulares', 'Acessórios', 'Notebooks', 'Acessórios', 'Monitores', 'Celulares', 'Acessórios'],
    'Quantidade': [1, 3, 1, 2, 1, 2, None], # Coloquei um None (NaN) de propósito para a sua explicação!
    'Preco_Unitario': [5000, 150, 8000, 350, 1200, 5000, 150],
    'Regiao': ['Sudeste', 'Sul', 'Sudeste', 'Nordeste', 'Centro-Oeste', 'Nordeste', 'Sul']
}
df = pd.DataFrame(dados)
# Salvando em CSV para os alunos usarem pd.read_csv()

#df.to_csv('vendas_loja.csv', index=False) #index=False. Não tem uma coluna principal de dados
#print("Dataset criado com sucesso!")

df.to_excel('vendas_loja.xlsx', index=False)
print("Dataset criado com sucesso!")