import pandas as pd 

df = pd.read_csv('vendas_loja.csv')


#print(df.head()) 
#print(df.shape)
#print(df.dtypes)

# Faturamento total
total_vendas = df['Preco_Unitario'].sum()
# Preço médio dos produtos
preco_medio = df['Preco_Unitario'].mean()
print(f"Total: R$ {total_vendas:,.2f}")
print(f"Média: R$ {preco_medio:,.2f}")

# Produto mais caro e mais barato
mais_caro = df['Preco_Unitario'].max()
mais_barato = df['Preco_Unitario'].min()
# Maior e menor quantidade vendida
maior_qtd = df['Quantidade'].max()
menor_qtd = df['Quantidade'].min()
print(f"Mais caro: R$ {mais_caro}")
print(f"Mais barato: R$ {mais_barato}")
