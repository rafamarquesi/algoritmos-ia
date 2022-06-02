'''Utilizado nas vídeos aulas do professor Rafael Rossi (https://www.youtube.com/playlist?list=PLAHmHkSA6KkV1euSfT1YaE1rT-d8cXE-I)'''
# importações

'''Foi utilizado o repositório de word embeddings do NILC (http://nilc.icmc.usp.br/nilc/index.php/repositorio-de-word-embeddings-do-nilc)'''

#importando o KeyedVectors do gensim
from gensim.models import KeyedVectors

if __name__ == '__main__':
    # Carregando as word embeddings
    modelo_wv = KeyedVectors.load_word2vec_format('cbow_s50.txt')

    # Usando modelo
    print(modelo_wv.most_similar('computador'))
    print(modelo_wv.most_similar('carro'))
    print(modelo_wv.most_similar('automóvel'))
    print(modelo_wv.most_similar(positive=['tecnologia', 'telefone']))
    print(modelo_wv.get_vector('presidente'))