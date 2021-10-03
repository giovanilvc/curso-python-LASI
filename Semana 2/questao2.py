#Importando as bibliotecas
import pandas as pd
import numpy as np

#Criando os DFs
df1 = pd.read_excel("data_uc.xlsx")
df2 = pd.read_excel("data_ts.xlsx")

df1.head() #vizualizando os dados
df2.head() #vizualizando os dados

lista_presentes = []          #Armazena as UCs presentes
lista_nao_presentes = []      #Armazena as UCs não presentes

for index, row in df1.iterrows():
  if row["UC_TOT"] in list(df2["UC"]):
    lista_presentes.append(row['UC_TOT'])
  else:
    lista_nao_presentes.append(row["UC_TOT"])

#DF com as Unidades consumidoras não presentes
df3 = pd.DataFrame({"UC não presentes": lista_nao_presentes})
df3