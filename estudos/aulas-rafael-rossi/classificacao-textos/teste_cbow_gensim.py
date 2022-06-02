'''Utilizado nas vídeos aulas do professor Rafael Rossi (https://www.youtube.com/playlist?list=PLAHmHkSA6KkV1euSfT1YaE1rT-d8cXE-I)'''
# Importações

# Carregar e visualizar os dados
import pandas as pd

# Gensim: gerar as word embeddings
import gensim

# Spacy para pré-processar os textos
import spacy

# tqdm
from tqdm import tqdm

# Descomentar abaixo caso esteja rodando no colab
# from IPython import get_ipython
# def tqdm_clear(*args, **kwargs):
#     getattr(tqdm, '_instances', {}).clear()

def preprocessamento(texto):
    tokens = nlp(texto)
    return [token.lemma_.lower() for token in tokens if token.is_alpha and not token.is_stop]
    # return ' '.join([token.lemma_.lower() for token in tokens if token.is_alpha and not token.is_stop])

if __name__ == '__main__':
    # Carregar Reviews
    # df = pd.read_csv('AmazonFoodReviews.csv')
    # print(df.shape)

    # pré-processando o textos

    #Objeto pré-processado de textos
    nlp = spacy.load('en_core_web_sm', disable=['ner', 'parser'])

    tqdm.pandas()
    # Processando os tokens e salvando em um CSV
    # df['Tokens'] = df['Text'].progress_apply(preprocessamento)
    # df.to_csv('AmazonFoodReviewsWithTokens.csv', index=False)



    # Treinamento das Word Embeddings
    # df = pd.read_csv('AmazonFoodReviewsWithTokens.csv',
    #                  converters={'Tokens': lambda x: x.strip('[]').replace("'", "").split(', ')})
    # print(df.shape)
    ## Word2Vec
    ### Continuous Bag-Of-Words (SCBOW)
    # Gerando o modelo CBOW
    # modelo_cbow = gensim.models.Word2Vec(df['Tokens'], sg=0, min_count=5, window=10, vector_size=100)

    # Salvando o modelo
    # modelo_cbow.save('AmazonFoodReviews_model_w2v_cbow.model')
    # Salvando só as word embeddings
    # modelo_cbow.wv.save('AmazonFoodReviews_model_w2v_cbow.kv')

    # carregando modelo salvo
    modelo_cbow = gensim.models.Word2Vec.load('AmazonFoodReviews_model_w2v_cbow.model')
    # Carregando só as word embeddings
    # kv_cbow = gensim.models.KeyedVectors.load('AmazonFoodReviews_model_w2v_cbow.kv')

    # consulta por similaridade
    print(modelo_cbow.wv.most_similar('cheese', topn=20))

    # obtendo o vetor da palavra
    print(modelo_cbow.wv.get_vector('cheese').shape)

    print(modelo_cbow.wv.most_similar(positive=['avocado'],topn=1))

    print(modelo_cbow.wv.most_similar(positive=['avocado','salsa'],topn=1))

    print(modelo_cbow.wv.most_similar(positive=['avocado', 'salsa'], negative=['salt'], topn=1))

    print(modelo_cbow.wv.most_similar(positive=['lemon', 'water'], topn=1))

    print('asdasd' in modelo_cbow.wv.key_to_index)



    # Gerando o modelo Skip-Gram
    # modelo_sg = gensim.models.Word2Vec(df['Tokens'], sg=1, min_count=5, window=10, vector_size=100)

    # Salvando o modelo
    # modelo_sg.save('AmazonFoodReviews_model_w2v.model')

    # carregando modelo salvo
    modelo_sg = gensim.models.KeyedVectors.load('AmazonFoodReviews_model_w2v.model')

    print(modelo_sg.wv.most_similar('cheese', topn=20))

    print(modelo_sg.wv.most_similar(positive=['lemon', 'water'], topn=1))

    # Gerando o modelo Fast Text
    # modelo_ft = gensim.models.FastText(df['Tokens'], sg=1, min_count=5, window=10, vector_size=100)

    # Salvando o modelo
    # modelo_ft.save('AmazonFoodReviews_model_ft.model')

    # carregando modelo salvo
    modelo_ft = gensim.models.FastText.load('AmazonFoodReviews_model_ft.model')

    print(modelo_ft.wv.most_similar('cheese', topn=20))

    print(modelo_ft.wv.get_vector('cheese'))