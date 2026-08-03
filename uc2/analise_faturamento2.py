import pandas as pd #primeiro vem sempre a importação

faturamento = pd.Series(
    [23000, 15000, 18500],
    index=['Janeiro', 'Fevereiro', 'Março'] #linhas para nomear as posições da coluna.
)
print(faturamento['Janeiro'])

print(faturamento * 2)

print(pd.isna(faturamento))

#print (faturamento)
#print (faturamento["Janeiro"])

#print(faturamento.mean()) - média da coluna
#print(faturamento.sum()) - soma de todas as entradas
#print(faturamento.min()) - menor valor
#print(faturamento.max()) - maior valor