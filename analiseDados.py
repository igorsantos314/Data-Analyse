import pandas as pd

#carrega o dataset
df = pd.read_csv("/home/igor/meus_projetos/supermarket_sales - Sheet1.csv")

#exibe
print(df.head())

#exibe a o maior valor da coluna Total
print(df["Total"].max())

#exibe a maior venda
print(df.max())

#tipo de cada coluna
print(df.dtypes)

#quantidade de linhas com o valor 0
print(df.isnull().sum())

#Exibe a soma dos Totais de cada cidade
print(df.groupby("City")["Total"].sum())

#Ordena por total decrescente
print(df.sort_values(by="Total", ascending=False).head(2))

#Estatisca dos dados
print(df.describe())

#exibe apenas uma coluna
print(df["City"])

#exibe todas as linhas que contenha determinada informação
data = df.loc[df["Date"] == "2/25/2019"]
print(data.head())

#exibe a quantidade de generos em cada linah de produto
df.groupby("Product line")["Gender"].nunique()
