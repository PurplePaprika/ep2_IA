# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 19:03:24 2019

@author: PurplePaprika
"""

import csv
import sklearn
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as np
import random

def dividirDataset(dataset, proporcao): #proporcao = % da amostra que será usada de base (0<p<1)// retorna BASE, TESTE
    total = dataset.copy()
    nTeste = int (len(dataset) * (1 - proporcao))
    nBase = len(dataset) - nTeste
    datasetTeste = []

    for i in range(0,nTeste):
        rnd = random.randint(0 , len(total)-1)
        datasetTeste.append(total[rnd])
        total.remove(total[rnd])

    return total, datasetTeste


dados = []
dadosTeste = []
classes = []
classesTeste = []

with open("base.txt") as arquivo:
    leitorCsv = csv.reader(arquivo, delimiter=",")
    for linha in leitorCsv:
        dados.append(linha)


dados, dadosTeste = dividirDataset(dados, 0.7)

for l in dados:
    classes.append(l[-1])

for k in dadosTeste:
    classesTeste.append(k[-1])

dadosNP = np.array(dados).astype(np.float)[:,:-1]
classesNP = np.array(classes).astype(np.float).reshape(-1, 1)
dadosTesteNP = np.array(dadosTeste).astype(np.float)[:,:-1]
classesTesteNP = np.array(classesTeste).astype(np.float).reshape(-1, 1)

gauss = GaussianNB()

gauss.fit(dadosNP, classesNP.ravel())

predicoes = gauss.predict(dadosTesteNP)

print("Acurácia :",metrics.accuracy_score(classesTesteNP, predicoes))
