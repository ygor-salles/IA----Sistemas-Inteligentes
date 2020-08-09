#Exercicio Slide09 - Algoritmos Genéticos
#Nome: Ygor Salles Aniceto Carvalho - 2017014382

import random

print("Modelo de entrada:")
print("0 0 0 0 0 0 0 0 0 ... 0 ---> ou seja separe por espaço cada elemento do vetor de inteiro")
print("Digite seu modelo:")
input_modelo = input()
modelo = [int(i) for i in input_modelo.split()]
print("\nModelo: {}".format(modelo)+'\n')
tamanho_individual = len(modelo)
tamanho_populacional = 8
pais = 2
probabilidade_mutacao = 0.5

def individual(min, max):
	return[random.randint(min, max) for i in range(tamanho_individual)]

def funcaoPopulacao():
	return[individual(0,7) for i in range(tamanho_populacional)]

def aptidao(individual):
	aptidao = 0
	for i in range(len(individual)):
		if(individual[i] == modelo[i]):
			aptidao += 1
	return aptidao

def taxaCruzamento(populacao):
	pontuados = [(aptidao(i), i) for i in populacao]
	pontuados = [i[1] for i in sorted(pontuados)]
	populacao = pontuados
	selecionados = pontuados[(len(pontuados) - pais):]
	for i in range(len(populacao) - pais):
		pontos = random.randint(1, tamanho_individual - 1)
		pai = random.sample(selecionados, 2)
		populacao[i][:pontos] = pai[0][:pontos]
		populacao[i][pontos:] = pai[1][pontos:]
	return populacao

def taxaMutacao(populacao):
	for i in range(len(populacao) - pais):
		if(random.random() <= probabilidade_mutacao):
			pontos = random.randint(0, tamanho_individual - 1)
			novo_valor = random.randint(1, 9)
			while(novo_valor == populacao[i][pontos]):
				novo_valor = random.randint(1,9)
			populacao[i][pontos] = novo_valor
	return populacao

populacao = funcaoPopulacao()
print("População Inicial: {}".format(populacao))
print("\n")
for i in range(100):
	populacao = taxaCruzamento(populacao)
	populacao = taxaMutacao(populacao)
print("População Final: {}".format(populacao))