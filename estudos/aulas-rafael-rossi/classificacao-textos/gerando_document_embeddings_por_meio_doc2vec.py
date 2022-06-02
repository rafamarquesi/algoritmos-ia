'''Utilizado nas vídeos aulas do professor Rafael Rossi (https://www.youtube.com/playlist?list=PLAHmHkSA6KkV1euSfT1YaE1rT-d8cXE-I)'''
# Importações

# utilitários para manipulação dos dados
import pandas as pd
import numpy as np

# Gerar as word embeddings
from gensim.models.doc2vec import Doc2Vec, TaggedDocument

# Pré-processamento (padronização e limpeza)
import spacy

# Construção do modelo e avaliação
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import f1_score

if __name__ == '__main__':
    # Carregando o dataset
    df = pd.read_csv('bbc-text.csv', nrows=400)
    print(df['category'].unique())

    df_treino, df_teste = train_test_split(df, test_size=0.3, stratify=df['category'])
    print(df_treino)
    print('----------------------------------')
    print(df_teste)
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    print(df_treino.groupby('category').count())
    print('----------------------------------')
    print(df_teste.groupby('category').count())

    # Pré-processamento dos textos
    nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])

    def preprocessamento(texto):
        return [token.lemma_.lower() for token in nlp(texto) if token.is_alpha and not token.is_stop]

    def tagged_data(textos):
        return [TaggedDocument(words=preprocessamento(text), tags=[str(i)]) for i, text in enumerate(textos)]

    def construir_vetores_treino(modelo, tagged_data, num_dim):
        matrix = np.zeros((len(tagged_data), num_dim))
        for i in range(len(tagged_data)):
            matrix[i] = modelo.docvecs[tagged_treino[i][1][0]]
        return matrix


    def construir_vetores_teste(modelo, tagged_data, num_dim):
        matrix = np.zeros((len(tagged_data), num_dim))
        for i in range(len(tagged_data)):
            matrix[i] = modelo.infer_vector(tagged_data[i][0])
        return matrix

    # print(tagged_data(df_treino['text']))

    # Gerando a represenação do conjunto de treino

    #Número de dimensões
    num_dimensoes = 100

    tagged_treino = tagged_data(df_treino['text'])

    #Criando o objeto do modelo
    modelo = Doc2Vec(vector_size=100, min_count=2, dm=1, epochs=100)

    #Obtendo os one-hot encoddings das palavras e documentos
    modelo.build_vocab(tagged_treino)

    #Treinando o modelo
    modelo.train(tagged_treino, total_examples=modelo.corpus_count, epochs=modelo.epochs)

    #Reduzindo o uso de memória (na versão do gensim 4, não tem o método)
    # modelo.delete_temporary_training_data(keep_doctags_vectors=True, keep_inference=True)

    # print(modelo.docvecs['57'])

    repr_treino = construir_vetores_treino(modelo, tagged_treino, num_dimensoes)

    print(repr_treino.shape)

    #Construindo o modelo de Classificação no Treino
    classificador = SVC(kernel='linear')
    classificador.fit(repr_treino, df_treino['category'])

    #Testando no Teste
    tagged_test = tagged_data(df_teste['text'])

    repr_teste = construir_vetores_teste(modelo, tagged_test, num_dimensoes)
    # print(repr_teste)
    print(repr_teste.shape)

    predicoes = classificador.predict(repr_teste)
    # print(predicoes)

    print(f1_score(df_teste['category'], predicoes, average='macro'))

