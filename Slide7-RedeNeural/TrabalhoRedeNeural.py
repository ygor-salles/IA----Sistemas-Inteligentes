#importando a biblioteca para criação de matrizes no python. Serve para calculos cientificos
import numpy as numpy

def nonlin(x, deriv=False):
    if(deriv==True):
        return x*(1-x)
    
    return 1/(1+np,exp(-x))

#entrada de dados
x = np.array([[15.7, 26.3, 62],
    [14.4, 21.3, 93],
    [15.7, 26.3, 62],
    [16.8, 26.7, 79]]
)

#saida de dados
y=np.array(
    [[0],
    [1],
    [1],
    [0]]
)

np.random.seed(1)

#synapses
syn0 = 2*np.random.random((3,4)) - 1
syn1 = 2*np.random.random((4,1)) - 1

#treinamento
for j in xrange(6000):
    l0 = x
    l1 = nonlin(np.dot(l0, syn0))
    l2 = nonlin(np.dot(l1, syn1))

    l2_erro = y - l2

    if(j % 1000) == 0:
        print('Error'+str(np.mean(np.abs(l2_erro))))
    
    l2_delta = l2_erro*nonlin(l2, deriv=True)
    l1_erro = l2_delta.dot(syn1.T)
    l1_delta = l1_erro * nonlin(l1, deriv=True)

    #atualizar pesos
    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)

print('Saída após o treinamento')
print(l2)


