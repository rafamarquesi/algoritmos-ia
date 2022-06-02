'''Utilizado nas vídeos aulas do professor Rafael Rossi (https://www.youtube.com/playlist?list=PLAHmHkSA6KkV1euSfT1YaE1rT-d8cXE-I)'''
#Importações
from gensim.models.phrases import Phraser, Phrases

import pandas as pd
import spacy
from sklearn.feature_extraction.text import CountVectorizer

#Configurações
pd.set_option('max_colwidth', 250)
nlp = spacy.load('en_core_web_sm')

#Pré-processamento
def tokenizador(texto):
    tokens = nlp(texto)
    return [token.lemma_.lower() for token in tokens if (not token.is_stop) and (token.is_alpha)]

def gera_lista_tokens(textos):
    lista = []
    for texto in textos:
        lista.append(tokenizador(texto))
    return lista

def preprocessador(texto):
    return ' '.join(phraser[tokenizador(texto)])

if __name__ == '__main__':
    #print(tokenizador('I want to try this tokenizer. 1989!'))

    #Coleção de Textos
    texts = [
        'Goku is a hero in the Dragon Ball since 1989! Goku saved the earth so many times.',
        'The 7 Dragon balls can make wishes come true! Each ball contains his own dragon.',
        'If the wishes are superfluous, the dragon balls will become dark.',
        'Seiya is a bronze knight and is one of the main Knights of the Zodiac. He saved Athena several times.',
        'A knight of the zodiac wear a bronze, silver or a gold cloth to protect Athena.',
        'Saint Seiya: Knights of the Zodiac is a Japanese manga in which mystical warriors called the Saints fight wearing sacred cloths.'
    ]
    classes = ['Dragon Ball', 'Dragon Ball', 'Dragon Ball', 'Cav. Zod.', 'Cav. Zod.', 'Cav. Zod.']

    df = pd.DataFrame({'texts': texts, 'classes': classes})

    # print(tokenizador(df['texts'].loc[0]))
    print(gera_lista_tokens(df['texts']))

    phrases = Phrases(gera_lista_tokens(df['texts']), min_count=1, threshold=1)
    phraser = Phraser(phrases)

    # novo_texto = 'Dragon ball is the best anime'
    # print(tokenizador(novo_texto))
    #
    # print(phraser[tokenizador(novo_texto)])
    #
    # print(' '.join(phraser[tokenizador(novo_texto)]))

    print(df['texts'].apply(preprocessador))

    df['texts_preproc'] = df['texts'].apply(preprocessador)

    #Vetorizando o texto

    vetorizador = CountVectorizer(min_df=2)
    representacao = vetorizador.fit_transform(df['texts_preproc'])

    print(vetorizador.vocabulary_)

    # Obtendo os termos ordenados de acordo com o seu índice no vocabulário
    colunas = [item[0] for item in sorted(vetorizador.vocabulary_.items(), key=lambda x: x[1])]
    print(colunas)

    # Gerando o DataFrame com os dados
    df_repr = pd.DataFrame(representacao.toarray(), columns=colunas)
    print(df_repr.shape)