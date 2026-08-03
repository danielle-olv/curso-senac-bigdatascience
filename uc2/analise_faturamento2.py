import pandas as pd #primeiro vem sempre a importação

faturamento = pd.Series(
    [23000, 15000, 18500],
    index=['Janeiro', 'Fevereiro', 'Março'] #linhas para nomear as posições da coluna.
)
print(faturamento['Janeiro'])

print(faturamento * 2)

print(pd.isna(faturamento))