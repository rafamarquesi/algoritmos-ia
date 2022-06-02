import numpy as np

# Importação de Métricas de Avaliação
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix
'''Arquivo com algumas funções para facilitar os cálculos na prova'''

def regressao_linear_fx(x:np, weights_thetas:np):
    '''calcula o f(x) para função linear'''
    linearFunction = x.dot(weights_thetas)
    # linearFunction = weights_thetas.dot(x.T)
    print('(Regressão linear) f(x): {}'.format(linearFunction))
    return linearFunction

def regressao_linear_custo_quadratico(dicionario:dict, m:int):
    '''Função de custo quadrático para regressão linear'''
    somatoria = 0
    for key, values in dicionario.items():
        somatoria = somatoria + ((values[0] - values[1])**2)
    print('(Regressão linear) Função de custo quadrático: {}'.format((1/(2*m)) * somatoria))

def regressao_linear_gradiente_descente_multivalorado(dicionario:dict, m:int, alfa:float, theta:float):
    '''Função que calcula o gradiente descendente multivalorado para regressão linear'''
    somatoria = 0
    for key, values in dicionario.items():
        somatoria = somatoria + ((values[0] - values[1]) * values[2])
    print('(Regressão linear) Novo valor para o Theta: {}'.format(theta - alfa * (1/m) * somatoria))

def regressao_logistica_fx_sigmoid(x:np, weights_thetas:np):
    sigmoidFunction = (1.0 / (1 + np.exp(-regressao_linear_fx(x=x, weights_thetas=weights_thetas))))
    print('(Regressão logistica) f(x): {}'.format(sigmoidFunction))
    return sigmoidFunction

def regressao_logistica_funcao_custo(dicionario:dict, m:int):
    '''Função de custo da regressão logística'''
    somatoria = 0
    for key, values in dicionario.items():
        somatoria = somatoria + (values[1] * np.log(values[0]) + (1 - values[1]) * np.log(1 - values[0]))
    print('(Regressão Logística) Função de custo: {}'.format(- (1 / m) * somatoria))

def redes_neurais_fx(x:list, theta:list):
    fx = 0
    for i in range(len(x)):
        fx = fx + (theta[i] * x[i])
    return fx

def redes_neurais_atualiza_peso_theta(theta:list, alfa:float, erro:float, x:list):
    novos_pesos = []
    for i in range(len(x)):
        novos_pesos.append(theta[i] + alfa * erro * x[i])
        # print('Novo valor para o Theta{}: {}'.format(i, ))
    return novos_pesos

def knn_normalizar_min_max(atributo:np):
    att_normalizado = np.zeros(shape=atributo.shape)
    for i in range(atributo.size):
        att_normalizado[i] = (atributo[i] - atributo.min()) / (atributo.max() - atributo.min())
    return att_normalizado

if __name__ == '__main__':
    # Primeria parte é para regressão linear e logistica
    # Descomentar abaixo para utilizar a regressão linear e logistica
    y = np.array([562.06, 625.93, 751.83, 983.22, 1116.44])
    x0 = np.array([1, 1, 1, 1, 1])
    x1 = np.array([10000, 20000, 30000, 40000, 50000])
    # x2 = [7.8, 4.3, 7.2, 8.6, 7.5]
    hx = []
    normalizar = True
    weights_thetas = np.array([0.4717215628269418, 0.7394729247086835])
    # Theta0: 0.4717215628269418 Theta1: 0.7394729247086835

    # # Normalizar os dados, caso os valores do conjunto sejam muito discrepantes
    if normalizar: # caso tenha mais atributos, crie mais abaixo
        x1 = knn_normalizar_min_max(atributo=x1)
        y = knn_normalizar_min_max(atributo=y)
        # x3 = knn_normalizar_min_max(atributo=x3)

    # TODO: descomentar as três linhas abaixo para calcular o f(x) da regressão linear
    for i in range(len(x0)):
        hx.append(regressao_linear_fx(x=np.array([x0[i], x1[i]]), weights_thetas=weights_thetas))
    print('(Regressão Linear) h(x): {}'.format(hx))
    # iteracao 1 hx = [1.0, 1.25, 1.5, 1.75, 2.0]
    # iteracao 2 hx = [0.4717215628269418, 0.6565897940041127, 0.8414580251812835, 1.0263262563584545, 1.2111944875356253]
    # iteracao 3 hx = [11.9546, 11.9748, 11.995, 12.0253, 12.0455]

    # Para calcular a função de custo quadrático da regressão linear deve-se passar um dicionário no seguinte
    # formato:
    # valores_erro_quadratico = {
    #   0 : [h(x), y],
    #   1 : [h(x), y]
    # }
    # onde h(x) é o valor calculado para f(x) e y é o y real
    # m = número de exemplos do conjunto
    # TODO: descomentar as três linhas abaixo para calcular a função de custo quadrático
    valores = {}
    for i in range(len(y)):
        valores[i] = [hx[i], y[i]]
    regressao_linear_custo_quadratico(dicionario=valores, m=5)
    # iteração 1: Função de custo quadrático: 0.5608697181290374

    # Para calcular o gradiente descente multivalorado da regressão linear deve-se passar um dicionário no seguinte
    # formato:
    # valores_gradiente = {
    #   0 : [h(x), y, x],
    #   1 : [h(x), y, x]
    # }
    # onde h(x) é o valor calculado para f(x) e y é o y real e x é o x real
    # m = número de exemplos do conjunto
    # theta = valor atual do theta
    # alfa = valor da taxa de aprendizagem
    # TODO: descomentar as três linhas abaixo para calcular o grandiente descente muiltivalorado
    for i in range(len(y)):
        valores[i] = [hx[i], y[i], x1[i]] # <---- Mudar o x para achar para achar os pesos de cada theta
    regressao_linear_gradiente_descente_multivalorado(dicionario=valores, m=5, alfa=0.5, theta=1)
    # Iteração 2: Theta0: 0.4717215628269418 Theta1: 0.7394729247086835
    # Iteração 3: Theta0: 0.9922950658416 Theta1: 0.9993389863857519






    # TODO: descomentar as três linhas abaixo para calcular o f(x) da regressão logistica
    # for i in range(len(x0)):
    #     hx.append(regressao_logistica_fx_sigmoid(x=np.array([x0[i], x1[i], x2[i]]), weights_thetas=weights_thetas))
    # print('(Regressão Logistica) h(x): {}'.format(hx))
    # iteração 1 h(x): h(x): [0.9999954482762552, 0.9997515449181605, 0.9999917062496261, 0.9999998321172752, 0.9999999245654222]
    # iteração 2 h(x): h(x): [0.9999933636662037, 0.9996866997769268, 0.9999881846930311, 0.9999997346113123, 0.9999998812838679]
    # iteracao 3 h(x): h(x): [0.9999903244148375, 0.9996049388259939, 0.9999831680015272, 0.9999995804775607, 0.9999998131705352]

    # Para calcular a função de custo da regressão logistica deve-se passar um dicionário no seguinte
    # formato:
    # valores_erro_quadratico = {
    #   0 : [h(x), y],
    #   1 : [h(x), y]
    # }
    # onde h(x) é o valor calculado para f(x) e y é o y real
    # m = número de exemplos do conjunto
    # TODO: descomentar as três linhas abaixo para calcular a função de custo
    # valores = {}
    # for i in range(len(y)):
    #     valores[i] = [hx[i], y[i]]
    # regressao_logistica_funcao_custo(dicionario=valores, m=5)
    # função de custo iteração 1 6.460052314956529
    # função de custo iteração 2 6.267482916910173
    # função de custo iteração 3 6.074920838321875

    # Para calcular o gradiente descente da regressão logistica deve-se passar um dicionário no seguinte
    # formato:
    # valores_gradiente = {
    #   0 : [h(x), y, x],
    #   1 : [h(x), y, x]
    # }
    # onde h(x) é o valor calculado para f(x) e y é o y real e x é o x real
    # m = número de exemplos do conjunto
    # theta = valor atual do theta
    # alfa = valor da taxa de aprendizagem
    # TODO: descomentar as três linhas abaixo para calcular o grandiente descente muiltivalorado
    # for i in range(len(y)):
    #     valores[i] = [hx[i], y[i], x2[i]] # <---- Mudar o x para achar para achar os pesos de cada theta
    # regressao_linear_gradiente_descente_multivalorado(dicionario=valores, m=5, alfa=0.01, theta=0.9614023311697012)
    # iteracao 2: Theta0: 0.9940005230877466 Theta1: 0.9800015838552689 Theta2: 0.9614023311697012
    # iteracao 3: Theta0: 0.9880011873596839 Theta1: 0.9600035978784719 Theta2: 0.9228053055642746





    # TODO: auxilio para calculo de perceptron simples, de rede neural
    # Redes Neurais
    # y = [0, 0, 0, 1]
    # x0 = [1, 1, 1, 1]
    # x1 = [0, 0, 1, 1]
    # x2 = [0, 1, 0, 1]
    # hx = []
    # weights_thetas = [-1.0, 1.0, 0.5]
    # alfa = 0.5
    # erro = 0
    #
    # for i in range(len(y)):
    #     hx.append(redes_neurais_fx(x=[x0[i], x1[i], x2[i]], theta=weights_thetas)) # <-- se tiver mais de um x, aumentar aqui
    #     # Aplicar função degrau
    #     if hx[i] <= 0:
    #         hx[i] = 0
    #     else:
    #         hx[i] = 1
    #     print('Entrada {}: Sout: h(x{})={}'.format(i + 1, i + 1, hx[i]))
    #     # Verificar se hx é diferente do y
    #     if hx[i] != y[i]:
    #         erro = y[i] - hx[i]
    #         print('h(x{}) é diferente de y{}! Atualizar pesos! Valor do erro: {}'.format(i + 1, i + 1, erro))
    #         print('Atualizando pesos!')
    #         weights_thetas = redes_neurais_atualiza_peso_theta(theta=weights_thetas, alfa=alfa, erro=erro, x=[x0[i], x1[i], x2[i]]) # <-- se tiver mais de um x, aumentar aqui
    #         print('Novos pesos: {}'.format(weights_thetas))








    # TODO: auxílio nos calculos de KNN (K vizinhos próximos)
    # KNN (K vizinhos próximos)
    # y = np.array([1, 0, 1, 0, 1, 0, 0, None, None, None])
    # x1 = np.array([4, 10, 3, 8, 10, 7, 6, 2, 10, 8])
    # x2 = np.array([100, 7, 50, 33, 80, 20, 60, 58, 7, 15])
    # x3 = np.array([10, 50, 20, 55, 82, 21, 122, 22, 50, 67])
    # normalizar = True
    #
    # # Normalizar os dados, caso os valores do conjunto sejam muito discrepantes
    # if normalizar: # caso tenha mais atributos, crie mais abaixo
    #     x1 = knn_normalizar_min_max(atributo=x1)
    #     x2 = knn_normalizar_min_max(atributo=x2)
    #     x3 = knn_normalizar_min_max(atributo=x3)
    # # Encontrar a posição do primeiro que está sem classe
    # posicao = 9 # posição que deseja realizar a classficação
    # # for i in range(len(y)):
    # #     if y[i] is None:
    # #         posicao = i
    # #         break
    # # calculo da distância
    # # somatoria = 0
    # for i in range(len(y)):
    #     if y[i] is None:
    #         break
    #     distancia = np.sqrt((x1[posicao] - x1[i])**2 + (x2[posicao] - x2[i])**2 + (x3[posicao] - x3[i])**2)
    #     print('Distância d({},{}): {}'.format(posicao+1, i+1, distancia))







    # calcular métricas de avaliação como matriz de confusão, acurácia, etc.
    # y_real = np.array([1, 0, 1, 0, 1, 0, 0, 1, 0, 0])
    # y_predito = np.array([1, 0, 1, 0, 1, 0, 0, 1, 0, 0]) # para 1 vizinho
    # y_predito = np.array([1, 0, 1, 0, 1, 0, 0, 1, 0, 0])  # para 3 vizinhos
    # print('Matriz de Confusão: {}'.format(confusion_matrix(y_true=y_real, y_pred=y_predito)))
    # print('Acuràcia: {}'.format(accuracy_score(y_true=y_real, y_pred=y_predito)))
    # print('Precisão: {}'.format(precision_score(y_true=y_real, y_pred=y_predito)))
    # print('Revocação: {}'.format(recall_score(y_true=y_real, y_pred=y_predito)))






    # TODO: abaixo está o algoritmo para o K-means
    # K-means
    # x1 = np.array([1, 2, 1, 2, 8, 9, 9, 8, 1, 2, 1, 2])
    # x2 = np.array([2, 1, 1, 2, 9, 8, 9, 8, 15, 15, 14, 14])
    # k = 3
    # centroides = {
    #     'c1': np.array([6, 6]),
    #     'c2': np.array([4, 6]),
    #     'c3': np.array([5, 10])
    # }
    #
    # # calcula a distância euclidiana
    # for i in range(len(x1)):
    #     menor_distancia = [9999999999999999999999, []]
    #     for key, centroide in centroides.items():
    #         distancia = np.sqrt((centroide[0] - x1[i]) ** 2 + (centroide[1] - x2[i]) ** 2)
    #         print('Distância centroide ({}) para ({},{}): {}'.format(centroide, x1[i], x2[i], distancia))
    #         if distancia < menor_distancia[0]:
    #             menor_distancia[0] = distancia
    #             menor_distancia[1] = centroide
    #     print('O ponto ({},{}) pertence ao grupo do centroide {}\n'.format(x1[i], x2[i], menor_distancia[1]))

