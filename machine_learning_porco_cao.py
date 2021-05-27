# -*- coding: utf-8 -*-
"""machine_learning - porco_cao

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16-gK8dB1a9YgK_65pC8N-z5HX8oSAZ0e
"""

#features (1 sim, 0 nao)
# pelo longo? perna curta? late?

porco1 = [0, 1, 0]
porco2 = [0, 1, 0]
porco3 = [1, 1, 0]

cachorro1 = [0, 1, 1]
cachorro2 = [1, 0, 1]
cachorro3 = [1, 1, 1]

#f(x) = y
# x = dados e y = classificacao

train_x = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]
#1 => porco, 0 => cachorro
train_y = [ 1, 1, 1, 0, 0, 0] #labels

#classificador 
from sklearn.svm import LinearSVC

model = LinearSVC()

#treinando de acordo com as classificações
model.fit(train_x,  train_y)

#dando um exemplo
animal_misterioso = [1,1,1]
model.predict([animal_misterioso])

#testando 
misterio1 = [1, 1, 1]
misterio2 = [1, 1, 0]
misterio3 = [0, 1, 1]

test_x = [misterio1, misterio2, misterio3]
test_y = [0,1,1]

previsoes = model.predict(test_x)

#calculando a taxa de acertos calculada

corretos = (previsoes == test_y).sum()
total = len(test_x)
taxa_acertos = corretos / total 
print("taxa de acertos calculada: %.2f " % (taxa_acertos * 100))

#calculando taxa de acertos através de método

from sklearn.metrics import accuracy_score
taxa_acertos = accuracy_score(test_y, previsoes)
print("taxa de acertos calculada por metodo: %.2f " % (taxa_acertos * 100))