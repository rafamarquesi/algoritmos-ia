"""
grafo_mapa = {
    "Araraquara": ["Belo Horizonte", "São Carlos", "Ribeirão Preto"],
    "Belo Horizonte": ["Araraquara", "São Carlos", "Três Lagoas", "São Paulo"],
    "São Carlos": ["Araraquara", "Belo Horizonte", "Três Lagoas", "Campinas", "Ribeirão Preto"],
    "Ribeirão Preto": ["Araraquara", "São Carlos", "Campo Grande"],
    "Campo Grande": ["Três Lagoas", "Ribeirão Preto"],
    "Três Lagoas": ["Campo Grande", "São Carlos", "Belo Horizonte", "São Paulo"],
    "São Paulo": ["Belo Horizonte", "Três Lagoas", "Campinas"],
    "Campinas": ["São Paulo", "São Carlos"]
}
Mostre as árvores de busca e a agenda, passo a passo, considerando que uma pessoa está
em Belo Horizonte e deseja chegar a Campo Grande, utilizando: (a)busca em largura;
(b)busca em profundidade; (c)busca em profundidade limitada iterativa
"""

grafo_mapa = {
    "Araraquara": ["Belo Horizonte", "São Carlos", "Ribeirão Preto"],
    "Belo Horizonte": ["Araraquara", "São Carlos", "Três Lagoas", "São Paulo"],
    "São Carlos": ["Araraquara", "Belo Horizonte", "Três Lagoas", "Campinas", "Ribeirão Preto"],
    "Ribeirão Preto": ["Araraquara", "São Carlos", "Campo Grande"],
    "Campo Grande": ["Três Lagoas", "Ribeirão Preto"],
    "Três Lagoas": ["Campo Grande", "São Carlos", "Belo Horizonte", "São Paulo"],
    "São Paulo": ["Belo Horizonte", "Três Lagoas", "Campinas"],
    "Campinas": ["São Paulo", "São Carlos"]
}

def busca_em_largura(grafo_mapa:dict, vertice_origem, vertice_destino):
    fila = []
    largura = {}
    count_largura = 1
    pai = {}
    nivel = {}
    aresta = {}
    caminhos_ate_destino = {}
    count_caminhos_encontrados = 0

    fila.append(vertice_origem)
    largura[vertice_origem] = count_largura
    pai[vertice_origem] = None
    nivel[vertice_origem] = 1

    while len(fila):
        print('Fila: {}'.format(fila))
        vertice = ''
        aux = []
        aux.append(fila.pop(0))
        while len(aux):
            if type(aux[0]) == str:
                vertice = aux[0]
                break
            else:
                aux = aux.pop(0)
                # print('Aqui ---> {}'.format(aux))
        # vertice = fila.pop(0)

        for vizinho in grafo_mapa.get(vertice):
            caminho = aux.copy()
            # print('Este é o aux ->>>> {}'.format(aux))
            # caminho.append(aux)
            if not largura.get(vizinho):
                caminho.insert(0, vizinho)
                #fila.append(vizinho)
                fila.append(caminho.copy())
                count_largura += 1
                largura[vizinho] = count_largura
                pai[vizinho] = vertice
                nivel[vizinho] = nivel[vertice] + 1

            if vizinho == vertice_destino and any(vizinho in c for c in caminho):
                count_caminhos_encontrados += 1
                caminho.reverse()
                caminhos_ate_destino[count_caminhos_encontrados] = caminho
            elif vizinho == vertice_destino and not any(vizinho in c for c in caminho):
                count_caminhos_encontrados += 1
                caminho.insert(0, vizinho)
                caminho.reverse()
                caminhos_ate_destino[count_caminhos_encontrados] = caminho

            print('%s -> %s:' % (str(vertice), str(vizinho)))
            if pai[vizinho] == vertice or pai[vertice] == vizinho:
                aresta[(vertice, vizinho)] = 'aresta de arvore'
                #print('aresta de arvore')
            elif nivel[vertice] == nivel[vizinho]:
                if pai[vertice] == pai[vizinho]:
                    aresta[(vertice, vizinho)] = 'aresta irma'
                    #print('aresta irma')
                else:
                    aresta[(vertice, vizinho)] = 'aresta primo'
                    #print('aresta primo')
            else:
                if nivel[vertice] < nivel[vizinho]:
                    aresta[(vertice, vizinho)] = 'aresta tia'
                    #print('aresta tia')
                else:
                    aresta[(vertice, vizinho)] = 'aresta sobrinha'
                    #print('aresta sobrinha')

        print('************************')

    # caminhos_ate_destino.append(vertice_destino)
    # fila.append(vertice_destino)
    # while len(fila):
    #     filho = fila.pop(0)
    #     if pai[filho] is not None:
    #         caminho_ate_destino.append(pai[filho])
    #         fila.append(pai[filho])

    # caminhos_ate_destino.reverse()
    # print('\nPrimeiro caminho mais curto encontrado até o destino {}'.format(caminho_ate_destino))

    return largura, pai, aresta, nivel, caminhos_ate_destino

def busca_em_profundidade(grafo_mapa:dict, vertice_origem, vertice_destino):
    fila = []
    largura = {}
    count_largura = 1
    pai = {}
    nivel = {}
    aresta = {}
    caminhos_ate_destino = {}
    count_caminhos_encontrados = 0

    fila.append(vertice_origem)
    largura[vertice_origem] = count_largura
    pai[vertice_origem] = None
    nivel[vertice_origem] = 1

    while len(fila):
        print('Fila: {}'.format(fila))
        vertice = ''
        aux = []
        aux.append(fila.pop(0))
        while len(aux):
            if type(aux[0]) == str:
                vertice = aux[0]
                break
            else:
                aux = aux.pop(0)
                # print('Aqui ---> {}'.format(aux))
        # vertice = fila.pop(0)

        for vizinho in grafo_mapa.get(vertice):
            # caminho = []
            caminho = aux.copy()
            # print('Este é o aux ->>>> {}'.format(aux))
            # print('Este é o caminho ->>>> {}'.format(caminho))
            # caminho.append(aux)
            if not largura.get(vizinho):
                caminho.insert(0, vizinho)
                print('este é caminho que vai para FILA: {}'.format(caminho))
                #fila.append(vizinho)
                # fila.append(caminho)
                fila.insert(0, caminho.copy())
                count_largura += 1
                largura[vizinho] = count_largura
                pai[vizinho] = vertice
                nivel[vizinho] = nivel[vertice] + 1

            if vizinho == vertice_destino and any(vizinho in c for c in caminho):
                count_caminhos_encontrados += 1
                caminho.reverse()
                caminhos_ate_destino[count_caminhos_encontrados] = caminho
            elif vizinho == vertice_destino and not any(vizinho in c for c in caminho):
                count_caminhos_encontrados += 1
                caminho.insert(0, vizinho)
                caminho.reverse()
                caminhos_ate_destino[count_caminhos_encontrados] = caminho
            # print('Este é o aux 2 ->>>> {}'.format(aux))
            # print('Este é o caminho 2 ->>>> {}'.format(caminho))

            print('%s -> %s:' % (str(vertice), str(vizinho)))
            if pai[vizinho] == vertice or pai[vertice] == vizinho:
                aresta[(vertice, vizinho)] = 'aresta de arvore'
                #print('aresta de arvore')
            elif nivel[vertice] == nivel[vizinho]:
                if pai[vertice] == pai[vizinho]:
                    aresta[(vertice, vizinho)] = 'aresta irma'
                    #print('aresta irma')
                else:
                    aresta[(vertice, vizinho)] = 'aresta primo'
                    #print('aresta primo')
            else:
                if nivel[vertice] < nivel[vizinho]:
                    aresta[(vertice, vizinho)] = 'aresta tia'
                    #print('aresta tia')
                else:
                    aresta[(vertice, vizinho)] = 'aresta sobrinha'
                    #print('aresta sobrinha')

        print('************************')

    # caminhos_ate_destino.append(vertice_destino)
    # fila.append(vertice_destino)
    # while len(fila):
    #     filho = fila.pop(0)
    #     if pai[filho] is not None:
    #         caminho_ate_destino.append(pai[filho])
    #         fila.append(pai[filho])

    # caminhos_ate_destino.reverse()
    # print('\nPrimeiro caminho mais curto encontrado até o destino {}'.format(caminho_ate_destino))

    return largura, pai, aresta, nivel, caminhos_ate_destino

def busca_em_profundidade_limitada_iterativa(grafo_mapa:dict, vertice_origem, vertice_destino):
    encontrou_destino = False
    l = 1
    while not encontrou_destino:
        print('ESTE É O L: {}'.format(l))
        fila = []
        largura = {}
        count_largura = 1
        pai = {}
        nivel = {}
        aresta = {}
        caminhos_ate_destino = {}
        count_caminhos_encontrados = 0

        fila.append(vertice_origem)
        largura[vertice_origem] = count_largura
        pai[vertice_origem] = None
        nivel[vertice_origem] = 1

        while len(fila):
            print('Fila: {}'.format(fila))
            vertice = ''
            aux = []
            aux.append(fila.pop(0))
            while len(aux):
                if type(aux[0]) == str:
                    vertice = aux[0]
                    break
                else:
                    aux = aux.pop(0)
                    # print('Aqui ---> {}'.format(aux))
            # vertice = fila.pop(0)

            for vizinho in grafo_mapa.get(vertice):
                # caminho = []
                caminho = aux.copy()
                # print('Este é o aux ->>>> {}'.format(aux))
                # print('Este é o caminho ->>>> {}'.format(caminho))
                # caminho.append(aux)
                if not largura.get(vizinho):
                    caminho.insert(0, vizinho)
                    print('este é caminho que vai para FILA: {}'.format(caminho))
                    #fila.append(vizinho)
                    # fila.append(caminho)
                    fila.insert(0, caminho.copy())
                    count_largura += 1
                    largura[vizinho] = count_largura
                    pai[vizinho] = vertice
                    nivel[vizinho] = nivel[vertice] + 1

                if vizinho == vertice_destino and any(vizinho in c for c in caminho):
                    count_caminhos_encontrados += 1
                    caminho.reverse()
                    caminhos_ate_destino[count_caminhos_encontrados] = caminho
                elif vizinho == vertice_destino and not any(vizinho in c for c in caminho):
                    count_caminhos_encontrados += 1
                    caminho.insert(0, vizinho)
                    caminho.reverse()
                    caminhos_ate_destino[count_caminhos_encontrados] = caminho
                # print('Este é o aux 2 ->>>> {}'.format(aux))
                # print('Este é o caminho 2 ->>>> {}'.format(caminho))

                print('%s -> %s:' % (str(vertice), str(vizinho)))
                if pai[vizinho] == vertice or pai[vertice] == vizinho:
                    aresta[(vertice, vizinho)] = 'aresta de arvore'
                    #print('aresta de arvore')
                elif nivel[vertice] == nivel[vizinho]:
                    if pai[vertice] == pai[vizinho]:
                        aresta[(vertice, vizinho)] = 'aresta irma'
                        #print('aresta irma')
                    else:
                        aresta[(vertice, vizinho)] = 'aresta primo'
                        #print('aresta primo')
                else:
                    if nivel[vertice] < nivel[vizinho]:
                        aresta[(vertice, vizinho)] = 'aresta tia'
                        #print('aresta tia')
                    else:
                        aresta[(vertice, vizinho)] = 'aresta sobrinha'
                        #print('aresta sobrinha')

            print('************************')
            if count_caminhos_encontrados != 0:
                encontrou_destino = True
                break
            elif any(l == nivel[key] for key in nivel):
                l += 1
                break

    # caminhos_ate_destino.append(vertice_destino)
    # fila.append(vertice_destino)
    # while len(fila):
    #     filho = fila.pop(0)
    #     if pai[filho] is not None:
    #         caminho_ate_destino.append(pai[filho])
    #         fila.append(pai[filho])

    # caminhos_ate_destino.reverse()
    # print('\nPrimeiro caminho mais curto encontrado até o destino {}'.format(caminho_ate_destino))

    return largura, pai, aresta, nivel, caminhos_ate_destino

if __name__ == '__main__':
    origem = 'Belo Horizonte'
    destino = 'Campo Grande'
    # Busca em LARGURA
    # largura, pai, aresta, nivel, caminhos_ate_destino = busca_em_largura(grafo_mapa, origem, destino)
    #
    # for key in caminhos_ate_destino:
    #     print('Caminho {}: {} de {} à {}.'.format(key, caminhos_ate_destino[key], origem, destino))

    # Busca em PROFUNDIDADE
    # largura, pai, aresta, nivel, caminhos_ate_destino = busca_em_profundidade(grafo_mapa, origem, destino)
    #
    # for key in caminhos_ate_destino:
    #     print('Caminho {}: {} de {} à {}.'.format(key, caminhos_ate_destino[key], origem, destino))

    # Busca em PROFUNDIDADE LIMITADA ITERATIVA
    largura, pai, aresta, nivel, caminhos_ate_destino = busca_em_profundidade_limitada_iterativa(grafo_mapa, origem, destino)

    for key in caminhos_ate_destino:
        print('Caminho {}: {} de {} à {}.'.format(key, caminhos_ate_destino[key], origem, destino))
