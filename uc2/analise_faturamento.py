import pandas as pd 

faturamento = pd.Series(
    [23000, 15000, 18500, None]
    index=["Janeiro", "Fevereiro", 'Março', "Abril"]
)

#print (faturamento)
#print (faturamento["Janeiro"])

#print(faturamento.mean()) - média da coluna
#print(faturamento.sum()) - soma de todas as entradas
#print(faturamento.min()) - menor valor
#print(faturamento.max()) - maior valor
