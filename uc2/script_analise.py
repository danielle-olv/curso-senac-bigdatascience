import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+mysqlconnector://root:@localhost:3306/ecommerce")
df_vendas = pd.read_sql("SELECT * FROM vendas_loja", con=engine)
df_frete = pd.read_sql("SELECT * FROM tabela_frete", con=engine)

print(df_vendas.head())
print("\n")
print(df_vendas.describe())
print("\n")
print(df_vendas.isna().sum())
print("\n")
total = df_vendas['Preco_Unitario'].sum()
print(f"O valor total é: R${total:,.2f}")
print("\n")
total = (df_vendas['Preco_Unitario']*df_vendas['Quantidade']).sum() #Medida iteradora
print(f"O faturamento total é R$: {total:,.2f}")
print("\n")
media = df_vendas['Preco_Unitario'].mean()
print(f"O valor médio é: R${media:,.2f}")
print("\n")
vmax = df_vendas['Preco_Unitario'].max()
print(f"O valor máximo unitário é: R${vmax:,.2F}")
print("\n")
vmin = df_vendas["Preco_Unitario"].min()
print(f"O valor mínimo unitário é: R${vmin:,.2f}")
print("\n")
df_fusao = pd.merge(
    df_vendas,              #Dataframe base (esquerda)
    df_frete,               #Dataframe a unir (direita)
    how="left",             #Chave da tabela da esquerda
    left_on="cod_regiao",   #Chave da tabela da direita
    right_on="regiao_id"    #Tipo de junção
)
df_fusao = df_fusao.drop(columns=['regiao_id']) #para retirar a informação duplicada
print(df_fusao.head())
print("\n")
print(df_fusao.shape)

df_fusao.to_excel("relatorio_vendas.xlsx", index=False)