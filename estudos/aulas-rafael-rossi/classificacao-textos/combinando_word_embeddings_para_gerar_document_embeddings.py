'''Utilizado nas vídeos aulas do professor Rafael Rossi (https://www.youtube.com/playlist?list=PLAHmHkSA6KkV1euSfT1YaE1rT-d8cXE-I)'''
# Importações

# utilitários para manipulação dos dados
import pandas as pd
import numpy as np

# Gerar as word embeddings
import gensim

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
    nlp = spacy.load('en_core_web_sm', disable=['parser','ner'])

    def preprocessamento(texto):
        return [token.lemma_.lower() for token in nlp(texto) if token.is_alpha and not token.is_stop]

    # preprocessamento do treino
    df_treino['tokens'] = df_treino['text'].apply(preprocessamento)

    # Gerando as representações
    # número de dimensões
    num_dimensoes = 100

    modelo_linguagem = gensim.models.Word2Vec(df_treino['tokens'], sg=0, min_count=2, window=10, vector_size=num_dimensoes, epochs=50)

    #print(modelo_linguagem.wv.index_to_key)

    def soma_vetores(tokens, num_dimensoes):
        vetor_texto = np.zeros(num_dimensoes)
        for token in tokens:
            try:
                vetor_texto += modelo_linguagem.wv.get_vector(token)
            except KeyError:
                continue
        return vetor_texto

    def construir_representacao(textos, num_dimensoes, metodo):
        matrix = np.zeros((len(textos), num_dimensoes))

        for i in range(len(textos)):
            tokens = textos.iloc[i]
            matrix[i] = soma_vetores(tokens, num_dimensoes)
            if metodo == 'average' and len(tokens) > 0:
                matrix[i] = matrix[i]/len(tokens)

        return matrix

    repr_treino = construir_representacao(df_treino['tokens'], num_dimensoes, 'sum')

    # Construindo um modelo de Classificação
    classificador = SVC(kernel='linear')
    classificador.fit(repr_treino, df_treino['category'])

    # Testando no conjunto de teste
    df_teste['tokens'] = df_teste['text'].apply(preprocessamento)

    repr_teste = construir_representacao(df_teste['tokens'], num_dimensoes, 'sum')

    predicoes = classificador.predict(repr_teste)

    print(f1_score(df_teste['category'], predicoes, average='macro'))

    # Comparando com a BOW
    from sklearn.feature_extraction.text import CountVectorizer
    vetorizador = CountVectorizer(min_df=2)

    bow_treino = vetorizador.fit_transform(df_treino['text'])

    classificador.fit(bow_treino, df_treino['category'])

    bow_teste = vetorizador.transform(df_teste['text'])

    predicoes = classificador.predict(bow_teste)

    print(f1_score(df_teste['category'], predicoes, average='macro'))