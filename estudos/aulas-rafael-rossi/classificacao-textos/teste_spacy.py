'''Utilizado nas vídeos aulas do professor Rafael Rossi (https://www.youtube.com/playlist?list=PLAHmHkSA6KkV1euSfT1YaE1rT-d8cXE-I)'''

#Importações
# python -m spacy download en_core_web_sm
import spacy

import pandas as pd
pd.set_option('max_colwidth', 250)
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

#Processador da Linguagem natural
nlp = spacy.load('en_core_web_sm')

if __name__ == '__main__':
    #Tokenização
    texto = 'Rafael is working at Google in the South America. He works very hard :D'

    tokens = nlp(texto)
    for token in tokens:
        print(token.text)

    print('------------<>-------------')

    sentencas = nlp(texto)

    for token in sentencas.sents:
        print(token)

    print('------------<>-------------')

    #Detectar Stopwords
    for token in tokens:
        print(f'{token.text} - {token.is_stop}')

    #Detectar tokens compostos por caracteres alfabéticos

    texto2 = 'Rafael is working at Google in the South America since 2010. He works 200 hours per week'

    tokens2 = nlp(texto2)

    print('------------<>-------------')

    for token in tokens2:
        print(f'{token.text} - {token.is_alpha}')

    print('------------<>-------------')

    #Simplificação das Palavras
    for token in tokens2:
        print(f'{token.text} - {token.lemma_}')

    print('------------<>-------------')

    #POS Tagging
    for token in tokens2:
        print(f'{token.text} - {token.pos_} - {token.tag_}')

    print('------------<>-------------')

    #Entidade Nomeadas
    for token in tokens2.ents:
        print(f'{token.text}')

    print('------------<>-------------')

    for token in tokens2.ents:
        print(f'{token.text} - {token.label_} - {spacy.explain(token.label_)}')

    print('------------<>-------------')

    #Integrando Spacy e ScikitLearn
    #Criando o objeto processador de linguagem natural
    nlp = spacy.load('en_core_web_sm')

    #Criando a função para preprocessar os textos
    def preprocessamento(texto):
        lista_final = []
        tokens = nlp(texto)
        for token in tokens:
            if (token.is_alpha and not token.is_stop):
                lista_final.append(token.lemma_.lower())
        return ' '.join(lista_final)

    texts = [
        'Goku is a hero in the Cragon Ball since 1989! Goku saved the earth so many times.',
        'The 7 Dragon balls can make wishes come true! Each ball contains his own dragon.',
        'If the wishes are superfluous, the dragon balls will become dark.',
        'Seiya is a bronze knight and is one of the main Knights of the Zodiac. He saved Athena several times.',
        'A knight of the zodiac wear a bronze, silver or a gold cloth to protect Athena.',
        'Saint Seiya: Knights of the Zodiac is a Japanese manga in which mystical warriors called the Saints fight wearing sacred cloths.'
    ]
    classes = ['Dragon Ball', 'Dragon Ball', 'Dragon Ball', 'Cav. Zod.', 'Cav. Zod.', 'Cav. Zod.']

    df = pd.DataFrame({'texts': texts, 'classes': classes})

    df['texts_preproc'] = df['texts'].apply(preprocessamento)

    vetorizador = CountVectorizer(min_df=2)

    representacao = vetorizador.fit_transform(df['texts_preproc'])

    print(representacao.toarray())

    #Obtendo os termos ordenados de acordo com o seu índice no vocabulário
    colunas = [item[0] for item in sorted(vetorizador.vocabulary_.items(), key=lambda x: x[1])]
    print(colunas)

    # Gerando o DataFrame com os dados
    df_repr = pd.DataFrame(representacao.toarray(), columns=colunas)
    print(df_repr.shape)