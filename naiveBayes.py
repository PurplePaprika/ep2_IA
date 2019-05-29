# -*- coding: utf-8 -*-
"""
Created on Tue May 28 19:03:24 2019

@author: PurplePaprika
"""

import csv
import random

def carregarDataset(arquivo):
	linhas = csv.reader(open(arquivo, "rt"))
	dataset = list(linhas)
	for i in range(len(dataset)):
		dataset[i] = [float(x) for x in dataset[i]]
	return dataset


dataset = carregarDataset('base.txt')
print (dataset)


def dividirDataset(dataset, proporcao): #proporcao = % da amostra que será usada de base (0<p<1)// retorna BASE, TESTE
    total = dataset.copy()
    nTeste = int (len(dataset) * (1 - proporcao))
    nBase = len(dataset) - nTeste
    datasetTeste = []

    for i in range (0,nTeste):
        rnd = random.randint(0 , len(total)-1)
        datasetTeste.append(total[rnd])
        total.remove(total[rnd])

    return total, datasetTeste


base, teste = dividirDataset(dataset, 0.7)

print (len(base), base)
print (len(teste), teste)
