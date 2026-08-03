import pandas as pd 

#Importação do CSV
df_vendas = pd.read_csv('vendas_loja.csv')

#Conversão de tipo explícita
df_vendas['Quantidade'] = pd.to_numeric(df_vendas['Quantidade'], errors='coerce')
df_vendas['Preco_Unitario'] = pd.to_numeric(df_vendas['Preco_Unitario'], errors='coerce')

#print(df_vendas.describe())

q1 = df_vendas['Preco_Unitario'].quantile(0.25)
q2 = df_vendas['Preco_Unitario'].quantile(0.50)
# q2 = df_vendas['Preco_Unitario'].median()
q3 = df_vendas['Preco_Unitario'].quantile(0.75)

# Intervalo Interquartil (Miolo estável)
iqr = q3 - q1

#print(iqr)

#Regra de Tukey (limites para encontrar outliers)
limite_sup = q3 + (1.5 * iqr)
limite_inf = q1 - (1.5 * iqr)

qtd_outliers = 0
for i in df_vendas['Preco_Unitario']:
    if(i>limite_sup or i<limite_inf):
        print(i)
        qtd_outliers += 1

print(f"O data set possui {qtd_outliers} na coluna Preco_Unitario")

df_limpo = df_vendas.query(
    'Preco_Unitario >= @limite_inf and '
    'Preco_Unitario <= @limite_sup'
)

print(f"Base limpa: {len(df_limpo)} registros")
print(df_limpo['Preco_Unitario'].describe())

#Outro exemplo de query(consulta) EXTRA
#media = df_limpo['Preco_Unitario'].mean()

#df_abaixo_media = df_limpo.query(
#'Preco_Unitario < @media')

#print(df_abaixo_media['Preco_Unitario'])