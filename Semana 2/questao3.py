#Importando as bibliotecas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import normalize, LabelEncoder

#Criando um DF com os dados
df = pd.read_csv("german_credit_data.csv", sep=';')
display(df)

#Separando dados de entrada e  saida
X = df[["Age", "Credit amount"]]
y = df["Risk"]
X_normalize = normalize(X)

#Separando grupo de treinamento e grupo de testes
X_train, X_test, y_train, y_test = train_test_split(X_normalize, y, test_size=0.1, random_state=0)

#Classificador KNN
clf = KNeighborsClassifier(n_neighbors=25, weights="uniform", leaf_size=50, metric='minkowski', p=2)

#Treinamento
clf.fit(X_train, y_train)

#Acurácia
accuracy_score(y_test, clf.predict(X_test))

# Seleciona no dataframe principal as linhas que possuem o risco desejado
good = df[df.Risk == 'good'] 
bad = df[df.Risk == 'bad']

#Gráfico
plt.scatter(good['Age'], good['Credit amount'], s=20,c='red')
plt.scatter(bad['Age'], bad['Credit amount'], s=20,c='black')

