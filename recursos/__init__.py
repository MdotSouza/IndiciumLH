#Módulo para manipulação das importações de arquivos

import pandas as pd
import os

def caminho():
	return "'\'recursos'\'" if os.name == "Windows" else "/recursos/"

def treino():
	treino = os.getcwd() + caminho() + 'cars_train.csv'
	return pd.read_csv(treino,sep="\t",encoding='UTF-16') 

def teste():
	test = os.getcwd() + caminho() + 'cars_test.csv'
	return pd.read_csv(test,sep="\t",encoding='UTF-16')

def treino_trat():
	treino = os.getcwd() + caminho() + 'cars_train_clean.csv'
	return pd.read_csv(treino,sep="\t",encoding='UTF-16') 	

def teste_trat():
	testLimpo = os.getcwd() + caminho() + 'cars_test_clean.csv'
	return pd.read_csv(testLimpo,sep="\t",encoding='UTF-16')