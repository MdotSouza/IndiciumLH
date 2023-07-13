#Módulo para manipulação das importações de arquivos

import pandas as pd
import os 

PATH = "'\'recursos'\'" if os.name == "Windows" else "/recursos/"

def treino():
	treino = os.getcwd() + PATH + 'cars_train.csv'
	return pd.read_csv(treino,sep="\t",encoding='UTF-16') 

def teste():
	test = os.getcwd() + PATH + 'cars_test.csv'
	return pd.read_csv(test,sep="\t",encoding='UTF-16')

def treinoLimpo():
	treino = os.getcwd() + PATH + 'cars_train_clean.csv'
	return pd.read_csv(treino,sep="\t",encoding='UTF-16') 	

def testeLimpo():
	testLimpo = os.getcwd() + PATH + 'cars_test_clean.csv'
	return pd.read_csv(testLimpo,sep="\t",encoding='UTF-16')