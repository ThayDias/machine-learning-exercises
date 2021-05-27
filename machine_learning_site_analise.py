# -*- coding: utf-8 -*-
"""machine_learning_site_analise

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZMqxpZV7QbhJTyawrubbvwoyiHfZJTZF
"""

#lendo uma planilha com pandas

import pandas as pd
uri='https://gist.githubusercontent.com/guilhermesilveira/2d2efa37d66b6c84a722ea627a897ced/raw/10968b997d885cbded1c92938c7a9912ba41c615/tracking.csv'
dados = pd.read_csv(uri)
dados.head()



#renomeando as colunas

mapa = {
    'home': 'principal',
    'how_it_works': 'como_funciona',
    'contact': 'contato',
    'bought': 'comprou'
}

dados = dados.rename(columns = mapa)

#separando as features da classificação 
#features, x

x = dados[["principal", "como_funciona", "contato"]]
print(x.head())

#classificacao, y

y = dados['comprou']
print(y.head())

dados.shape

#separando treino de teste 
#definindo 75 elementos para treino 
treino_x = x[:75]
treino_y = y[:75]

#definindo 25 elementos para teste
teste_x = x[75:]
teste_y = y[75:]

print("treino: ", len(treino_x), "teste: ", len(teste_x))

#treinando
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

model = LinearSVC()
model.fit(treino_x, treino_y)

#prevendo 
previsoes = model.predict(teste_x)
acuracia = accuracy_score(teste_y, previsoes) * 100
print("acurácia: %.2f%%" % acuracia)

"""#Usando biblioteca para separar Teste de treino"""

from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

#separando teste de treino
#random_state = gerando testes com numeros aleatorios 
#stratify = organizar proporcionalmente de acordo com as classificações

#numero inicial
SEED = 20

print("treino: ", len(treino_x), "teste: ", len(teste_x))
treino_x, teste_x, treino_y, teste_y = train_test_split(x, y,random_state = SEED, test_size = 0.25, stratify = y)

#treinando
model = LinearSVC()
model.fit(treino_x, treino_y)

#prevendo 
previsoes = model.predict(teste_x)
acuracia = accuracy_score(teste_y, previsoes) * 100
print("acurácia: %.2f%%" % acuracia)

#quantidade 0 e 1 treino
treino_y.value_counts()

#quantidade 0 e 1 treino
teste_y.value_counts()

